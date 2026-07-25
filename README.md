# Selenium Academy — Test Otomasyonu Öğrenme Projesi

[selenium.academy](https://selenium.academy/) eğitimini takip ederken, her
dersi Python + Selenium ile **çalışan test koduna** çevirdiğim uygulamalı repo.

**Yazan:** Anıl Kavak — [Portfolyo](https://anllkvk.github.io/) · TDG Corp
**Teknolojiler:** Python 3.12 · Selenium 4 · pytest

> 📘 Öğrenme günlüğü ve ilerleme takibi için **[GUIDE.md](GUIDE.md)** dosyasına bak.

---

## 🚀 Hızlı Başlangıç

```powershell
# 1) Depoyu klonla
git clone https://github.com/anllkvk/selenium.academy.git
cd selenium.academy

# 2) Sanal ortam kur ve aktifleştir
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3) Bağımlılıkları yükle
pip install -r requirements.txt

# 4) Testleri çalıştır
pytest
```

## 📁 Proje Yapısı

```
selenium.academy/
├── conftest.py          # Ortak pytest fixture'ları (driver, driver_fabrikasi)
├── pytest.ini           # pytest yapılandırması ve marker'lar
├── requirements.txt     # Python bağımlılıkları
├── tests/               # Her ders kendi klasöründe
│   ├── ders_01_kurulum/     # Ders 1: kurulum doğrulama
│   │   └── test_kurulum.py
│   ├── ders_02_locators/    # Ders 2: locator'lar & etkileşim
│   │   └── test_locators.py
│   └── ders_03_webdrivers/  # Ders 3: sürücüler, options, cross-browser
│       └── test_webdrivers.py
├── pages/               # Page Object Model sınıfları (ileride)
├── screenshots/         # Test ekran görüntüleri
├── notlar/              # Ders notlarının dijital hali
└── GUIDE.md             # Uygulamalı öğrenme rehberi + ders notları
```

## ▶️ Testleri Çalıştırma

```powershell
pytest                       # tüm testler (varsayılan tarayıcı: Chrome)
pytest --browser=edge        # Edge ile çalıştır
pytest --browser=firefox     # Firefox ile çalıştır
pytest --headless            # tarayıcı penceresi açmadan (CI modu)
pytest -m crossbrowser       # sadece cross-browser testleri
pytest -m smoke              # hızlı temel testler
```

## 📚 İşlenen Konular

| # | Konu | Durum |
|---|------|-------|
| 1 | Development Setup (ortam kurulumu) | ✅ |
| 2 | Locator'lar & ilk WebDriver etkileşimi | ✅ |
| 3 | WebDrivers Explained (options, headless, cross-browser) | ✅ |
| 4 | Bekleme (wait) türleri: implicit / explicit | ⏳ |
| 5 | Cookies (oluştur/oku/sil) | ⏳ |
| 6 | Screenshots | ⏳ |
| 7 | Page Object Model & Design Patterns | ⏳ |
| 8 | Flaky testlerden kaçınma | ⏳ |
| 9 | Selenium Grid | ⏳ |
| 10 | CI (Jenkins / TeamCity) | ⏳ |

## 📄 Lisans

Eğitim amaçlı kişisel öğrenme projesi.
