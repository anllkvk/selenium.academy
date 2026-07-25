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
git clone https://github.com/anllkvk/selenium-academy.git
cd selenium-academy

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
selenium-academy/
├── conftest.py          # Ortak pytest fixture'ları (driver aç/kapat)
├── pytest.ini           # pytest yapılandırması
├── requirements.txt     # Python bağımlılıkları
├── tests/               # Her ders kendi klasöründe
│   ├── ders_01_kurulum/     # Ders 1: kurulum doğrulama
│   │   └── test_kurulum.py
│   └── ders_02_locators/    # Ders 2: locator'lar & etkileşim
│       └── test_locators.py
├── pages/               # Page Object Model sınıfları (ileride)
├── screenshots/         # Test ekran görüntüleri
├── notlar/              # El yazısı ders notlarının dijital hali
└── GUIDE.md             # Uygulamalı öğrenme rehberi + notlar
```

## 📚 İşlenen Konular

| # | Konu | Durum |
|---|------|-------|
| 1 | Development Setup (ortam kurulumu) | ✅ |
| 2 | Cookies (oluştur/oku/sil) | ⏳ |
| 3 | Screenshots | ⏳ |
| 4 | Page Object Model & Design Patterns | ⏳ |
| 5 | Flaky testlerden kaçınma | ⏳ |
| 6 | Cross-browser testler | ⏳ |
| 7 | Selenium Grid | ⏳ |
| 8 | CI (Jenkins / TeamCity) | ⏳ |

## 📄 Lisans

Eğitim amaçlı kişisel öğrenme projesi.
