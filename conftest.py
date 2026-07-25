"""
conftest.py — pytest'in otomatik bulduğu ortak yapılandırma dosyası.

Buradaki 'fixture'lar tüm testlerde paylaşılır. En önemlisi 'driver' fixture'ı:
her test için bir tarayıcı açar, test bitince kapatır. Böylece her testte
tekrar tekrar tarayıcı açma/kapama kodu yazmayız (DRY prensibi).

Ders 3'ten sonra: artık Chrome'a sabit değiliz. Hangi tarayıcıda çalışacağımızı
komut satırından seçiyoruz:

    pytest                          # varsayılan: chrome
    pytest --browser=edge           # Edge ile çalıştır
    pytest --browser=firefox        # Firefox ile çalıştır (kuruluysa)
    pytest --headless               # tarayıcıyı görünmez modda çalıştır (CI için)
"""
import os
import shutil
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Desteklediğimiz tarayıcılar. Ders 3'ün özü: her tarayıcının kendi
# driver'ı (chromedriver/msedgedriver/geckodriver) ve kendi Options sınıfı var,
# ama bir kere driver nesnesini aldıktan sonra API tamamen aynı.
DESTEKLENEN_TARAYICILAR = ("chrome", "edge", "firefox")


def pytest_addoption(parser):
    """pytest'e kendi komut satırı seçeneklerimizi ekliyoruz."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Testlerin çalışacağı tarayıcı: chrome | edge | firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Tarayıcıyı ekranda göstermeden (görünmez) çalıştır.",
    )


def tarayici_kurulu_mu(tarayici: str) -> bool:
    """Bu makinede ilgili tarayıcı var mı? (Yoksa testi atlamak için kullanıyoruz.)"""
    yollar = {
        "chrome": [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ],
        "edge": [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ],
        "firefox": [
            r"C:\Program Files\Mozilla Firefox\firefox.exe",
            r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        ],
    }
    exe_adi = {"chrome": "chrome", "edge": "msedge", "firefox": "firefox"}[tarayici]
    if shutil.which(exe_adi):
        return True
    return any(os.path.exists(y) for y in yollar[tarayici])


def driver_olustur(tarayici: str = "chrome", headless: bool = False):
    """
    İstenen tarayıcı için bir WebDriver nesnesi üretir.

    Ders 3'ün kalbi burası:
      - Her tarayıcının ayrı bir Options sınıfı var (ChromeOptions, EdgeOptions...)
      - Headless argümanı bile tarayıcıya göre değişiyor
        (Chrome/Edge: '--headless=new', Firefox: '-headless')
      - Selenium 4.6+ ile gelen "Selenium Manager" doğru driver'ı (chromedriver,
        msedgedriver, geckodriver) otomatik indirir — elle indirmiyoruz.
    """
    tarayici = tarayici.lower()
    if tarayici not in DESTEKLENEN_TARAYICILAR:
        raise ValueError(
            f"Bilinmeyen tarayıcı: '{tarayici}'. "
            f"Seçenekler: {', '.join(DESTEKLENEN_TARAYICILAR)}"
        )

    if tarayici == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        drv = webdriver.Chrome(options=options)

    elif tarayici == "edge":
        # Edge, Chromium tabanlı olduğu için argümanları Chrome ile neredeyse aynı.
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        drv = webdriver.Edge(options=options)

    else:  # firefox
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")  # dikkat: tek tire
        drv = webdriver.Firefox(options=options)
        drv.maximize_window()  # Firefox'ta --start-maximized argümanı yok

    drv.implicitly_wait(5)  # element ararken 5sn'ye kadar bekle
    return drv


@pytest.fixture
def driver(request):
    """Her test için temiz bir tarayıcı açar ve test sonunda kapatır."""
    tarayici = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    drv = driver_olustur(tarayici, headless)
    yield drv  # test bu noktada çalışır
    drv.quit()  # test bitti, tarayıcıyı kapat


@pytest.fixture
def driver_fabrikasi():
    """
    Tek bir test içinde BİRDEN FAZLA tarayıcı açmak için fabrika fixture'ı.
    Cross-browser testlerinde kullanıyoruz. Açılan tüm tarayıcılar test
    bitince otomatik kapanır.

        def test_ornek(driver_fabrikasi):
            drv = driver_fabrikasi("edge", headless=True)
    """
    acilanlar = []

    def _olustur(tarayici: str = "chrome", headless: bool = False):
        drv = driver_olustur(tarayici, headless)
        acilanlar.append(drv)
        return drv

    yield _olustur

    for drv in acilanlar:
        drv.quit()


def save_screenshot(driver, name: str) -> str:
    """Ekran görüntüsünü screenshots/ klasörüne zaman damgasıyla kaydeder."""
    folder = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(folder, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(folder, f"{name}_{stamp}.png")
    driver.save_screenshot(path)
    return path
