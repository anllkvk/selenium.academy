"""
Ders 2 — İlk WebDriver Etkileşimi (Locator'lar + Aksiyonlar)

Kurulumun çalıştığını kanıtladık; şimdi Selenium'un ASIL işini öğreniyoruz:
1. Sayfada bir element BUL (locator)
2. O elemente bir AKSİYON uygula (tıkla, yaz)
3. Sonucu DOĞRULA (assert)

Hedef site: the-internet.herokuapp.com — otomasyon pratiği için yapılmış
güvenli bir test sitesi (gerçek/prod site değil, bilinçli seçildi).

Çalıştır:  pytest tests/test_01_ilk_etkilesim.py -v -s
"""
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_link_tiklama(driver):
    """Bir linki metnine göre bulup tıklıyoruz ve yeni sayfayı doğruluyoruz."""
    driver.get("https://the-internet.herokuapp.com/")

    # LOCATOR: linki görünen metnine göre bul
    form_link = driver.find_element(By.LINK_TEXT, "Form Authentication")
    form_link.click()  # AKSİYON: tıkla

    # DOĞRULAMA: login sayfasına geldik mi?
    baslik = driver.find_element(By.TAG_NAME, "h2").text
    assert baslik == "Login Page"
    print(f"\n[OK] Yönlendiği sayfa başlığı: {baslik}")


@pytest.mark.smoke
def test_form_doldur_ve_giris_yap(driver):
    """Kullanıcı adı/şifre alanlarını doldurup giriş yapıyoruz (başarılı senaryo)."""
    driver.get("https://the-internet.herokuapp.com/login")

    # LOCATOR: alanları id'lerine göre buluyoruz (en güvenilir locator id'dir)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # LOCATOR: giriş butonunu CSS seçici ile bul, tıkla
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # DOĞRULAMA: başarı mesajı çıktı mı?
    mesaj = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in mesaj
    print(f"\n[OK] Giriş başarılı mesajı alındı.")


@pytest.mark.smoke
def test_hatali_giris(driver):
    """Yanlış kullanıcı adıyla giriş denenince hata mesajı gösteriliyor mu?"""
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("yanlis_kullanici")
    driver.find_element(By.ID, "password").send_keys("yanlis_sifre")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mesaj = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in mesaj
    print(f"\n[OK] Hatalı giriş doğru şekilde reddedildi.")
