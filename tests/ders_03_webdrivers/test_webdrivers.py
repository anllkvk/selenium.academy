"""
Ders 3 — Selenium WebDrivers Explained (Sürücüler, Options, Cross-Browser)

Bu derste öğrendiğimiz üç şey:
  1. Her tarayıcının kendi SÜRÜCÜSÜ var (chromedriver, msedgedriver, geckodriver)
     ama driver nesnesini aldıktan sonra kullandığımız API aynı.
  2. OPTIONS ile tarayıcıyı açılmadan önce yapılandırıyoruz (headless, pencere
     boyutu, bildirimleri kapatma...).
  3. Aynı testi farklı tarayıcılarda çalıştırmak = CROSS-BROWSER test.

Çalıştır:
    pytest tests/ders_03_webdrivers -v -s
    pytest tests/ders_03_webdrivers --browser=edge -v
    pytest tests/ders_03_webdrivers --headless -v
"""
import pytest

from conftest import driver_olustur, tarayici_kurulu_mu

# Bu makinede kurulu olan tarayıcılar (Firefox yoksa otomatik elenir).
MEVCUT_TARAYICILAR = [t for t in ("chrome", "edge", "firefox") if tarayici_kurulu_mu(t)]

HEDEF = "https://the-internet.herokuapp.com/"


@pytest.mark.webdriver
@pytest.mark.smoke
def test_ortak_webdriver_api(driver):
    """
    Hangi tarayıcı olursa olsun WebDriver'ın temel komutları aynıdır:
    git, başlığı oku, adrese bak, ileri/geri/yenile.
    """
    driver.get(HEDEF)
    assert driver.title == "The Internet"
    assert driver.current_url.startswith("https://the-internet.herokuapp.com")

    # Başka bir sayfaya git
    driver.get(HEDEF + "login")
    assert "login" in driver.current_url

    # Tarayıcı geçmişinde gezin
    driver.back()
    assert driver.current_url.rstrip("/").endswith("herokuapp.com")

    driver.forward()
    assert "login" in driver.current_url

    driver.refresh()
    assert "login" in driver.current_url

    print(f"\n[OK] Ortak API çalıştı. Tarayıcı: {driver.name}")


@pytest.mark.webdriver
def test_options_ile_pencere_boyutu(driver_fabrikasi):
    """
    OPTIONS = tarayıcıyı açmadan önce verdiğimiz ayarlar.
    Burada pencere boyutunu biz belirliyoruz ve gerçekten uygulandığını
    doğruluyoruz.
    """
    drv = driver_fabrikasi("chrome", headless=True)  # headless'ta --window-size geçerli
    drv.get(HEDEF)

    boyut = drv.get_window_size()
    print(f"\n[OK] Pencere boyutu: {boyut['width']}x{boyut['height']}")
    assert boyut["width"] == 1920
    assert boyut["height"] == 1080


@pytest.mark.webdriver
def test_headless_modda_calisir(driver_fabrikasi):
    """
    Headless = tarayıcı arayüzü ekranda görünmeden çalışır.
    CI/CD ortamlarında (Jenkins, GitHub Actions) ekran olmadığı için şarttır.
    Test aynı işi yapar, sadece pencereyi görmeyiz.
    """
    drv = driver_fabrikasi("chrome", headless=True)
    drv.get(HEDEF)

    assert drv.title == "The Internet"
    # Headless Chrome kendini user-agent'ta belli eder:
    user_agent = drv.execute_script("return navigator.userAgent;")
    print(f"\n[OK] Headless çalıştı. User-Agent: {user_agent[:80]}...")
    assert "Chrome" in user_agent


@pytest.mark.webdriver
@pytest.mark.crossbrowser
@pytest.mark.parametrize("tarayici", MEVCUT_TARAYICILAR)
def test_cross_browser_giris(driver_fabrikasi, tarayici):
    """
    CROSS-BROWSER: Ders 2'deki login senaryosunun aynısını, bu makinede kurulu
    HER tarayıcıda çalıştırıyoruz. Tek satır kod değişmiyor — sadece driver.

    İş değeri: "Sitemiz Chrome'da çalışıyor ama Edge'de bozuk" tipi hataları
    kod yazmadan, tek testle yakalıyoruz.
    """
    from selenium.webdriver.common.by import By

    drv = driver_fabrikasi(tarayici, headless=True)
    drv.get(HEDEF + "login")

    drv.find_element(By.ID, "username").send_keys("tomsmith")
    drv.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    drv.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mesaj = drv.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in mesaj
    print(f"\n[OK] {tarayici.upper()} tarayıcısında giriş başarılı.")


@pytest.mark.webdriver
def test_bilinmeyen_tarayici_hata_verir():
    """
    Savunmacı kod kontrolü: desteklemediğimiz bir tarayıcı adı verilirse
    anlaşılır bir hata almalıyız (sessizce Chrome açmamalı).
    """
    with pytest.raises(ValueError, match="Bilinmeyen tarayıcı"):
        driver_olustur("netscape")

    print("\n[OK] Yanlış tarayıcı adı doğru şekilde reddedildi.")


# ---------------------------------------------------------------------------
# 📌 Ders notu — quit() vs close()
#
#   drv.close()  -> sadece AKTİF sekmeyi kapatır. Son sekmeyse tarayıcı kapanır
#                   ama driver süreci (chromedriver.exe) arkada asılı kalabilir.
#   drv.quit()   -> tüm sekmeleri kapatır VE driver sürecini sonlandırır.
#
#   Kural: test bitiminde her zaman quit() kullan. Aksi halde arka planda
#   onlarca chromedriver.exe birikir ve makine yavaşlar.
# ---------------------------------------------------------------------------
