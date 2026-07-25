"""
Ders 1 — Development Setup (Kurulum Doğrulama)

Bu ilk test, geliştirme ortamının doğru kurulduğunu kanıtlar:
- Selenium yüklü mü?
- Chrome açılıyor mu?
- Bir sayfaya gidip başlığını okuyabiliyor muyuz?

Çalıştırmak için (venv aktifken):
    pytest tests/test_00_setup.py
"""
import pytest


@pytest.mark.smoke
def test_selenium_kurulumu_calisiyor(driver):
    """Selenium tarayıcıyı açıp bir siteye gidebiliyor mu?"""
    driver.get("https://www.selenium.dev/")

    # Sayfa başlığında 'Selenium' geçmesini bekliyoruz
    assert "Selenium" in driver.title, f"Beklenmeyen başlık: {driver.title}"
    print(f"\n[OK] Sayfa başlığı: {driver.title}")


@pytest.mark.smoke
def test_python_org_baslik(driver):
    """İkinci bir doğrulama: python.org başlığını kontrol et."""
    driver.get("https://www.python.org/")
    assert "Python" in driver.title
    print(f"\n[OK] Sayfa başlığı: {driver.title}")
