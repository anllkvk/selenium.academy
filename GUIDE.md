# 🎓 Selenium.Academy — Uygulamalı Ders Rehberi

> Bu dosya, selenium.academy eğitimini işlerken **yanımda tuttuğum çalışma
> defterim**. Her dersi işlerken buraya notumu düşüyorum, öğrendiğimi `tests/`
> klasöründe çalışan koda çeviriyorum. Amaç: sertifika + LinkedIn paylaşımı +
> düzenli bir GitHub reposu.

**Öğrenci:** Anıl Kavak · [Portfolyo](https://anllkvk.github.io/)
**Şirket:** TDG Corp · [tdg-global.net](https://tdg-global.net/)
**Eğitim:** [selenium.academy](https://selenium.academy/) (Python)
**Başlangıç:** 2026-07-22

---

## 🛠️ Nasıl Çalışıyoruz? (her ders için rutin)

1. Dersi selenium.academy'de izle/oku.
2. Ders sırasında kendi notumu alırım → **notlarımı doğrudan Claude'a yazarım**
   (ders adı + ana başlıklar + gördüğüm kod). Site üye girişi istediği için
   içeriği benim aktarmam gerekiyor.
3. Bu dosyada ilgili dersin bölümüne **kısa dijital not** al (kendi cümlelerinle).
4. Öğrendiğini `tests/` altında yeni bir test dosyasına **koda dök**.
5. `pytest` ile çalıştır, yeşil olduğunu gör.
6. Anlamlı bir commit at (aşağıdaki git bölümüne bak).

> 📁 **notlar/** klasörü: el yazısı notlarımın fotoğrafları/yazılı hali burada.
> Kullanımı için `notlar/README.md` dosyasına bak.

> 🗂️ **Klasör kuralı:** Her dersin kodu `tests/ders_XX_konu/` altında ayrı
> klasörde durur (örn. `tests/ders_03_cookies/test_cookies.py`). Böylece repo
> ders ders düzenli kalır.

**Her oturum başında sanal ortamı aç:**
```powershell
cd "C:\Users\Anil Kavak\Desktop\selenium dersleri"
.\.venv\Scripts\Activate.ps1     # komut satırında (.venv) görürsün
```
> PowerShell script çalıştırmaya izin vermezse bir defalık:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Test çalıştırma komutları:**
```powershell
pytest                       # tüm testler
pytest tests/test_00_setup.py    # tek dosya
pytest -m smoke              # sadece 'smoke' işaretli testler
pytest -k cookie            # adında 'cookie' geçen testler
```

---

## 🗺️ Eğitim Yol Haritası (İlerleme Takibi)

Ders işledikçe kutucukları `[x]` yapıyorum.

### Bölüm 1 — Temeller
- [x] **Development Setup (Python)** — ortam kurulumu ✅ *(ders_01_kurulum/test_kurulum.py)*
- [x] İlk WebDriver testi — element bulma (find_element) ✅ *(ders_02_locators/test_locators.py)*
- [~] Locator stratejileri (id, name, css, xpath) — başladık (id, link_text, css, tag_name)
- [x] **WebDrivers Explained** — sürücüler, Options, headless, cross-browser ✅ *(ders_03_webdrivers/test_webdrivers.py)*
- [ ] Bekleme (wait) türleri: implicit / explicit

### Bölüm 2 — Tarayıcı Etkileşimleri
- [ ] **Cookies** — oluşturma, okuma, silme
- [ ] **Screenshots** — test sırasında ve hata anında ekran görüntüsü

### Bölüm 3 — Sürdürülebilir Testler (Maintainable Tests)
- [ ] **Design Patterns** — Page Object Model (POM), Page Factory
- [ ] **Flaky testlerden kaçınma** — rastgele başarısızlıkları önleme
- [ ] **Cross-Browser** testler

### Bölüm 4 — Selenium Grid (dağıtık çalıştırma)
- [ ] Selenium Grid'e giriş
- [ ] Bulut sağlayıcılar: CrossBrowserTesting / SauceLabs / TestingBot
- [ ] BrowseEmAll (on-premise)

### Bölüm 5 — Test Framework'leri
- [ ] Watir · Protractor · Galen

### Bölüm 6 — Continuous Integration (CI)
- [ ] Jenkins ile Selenium
- [ ] TeamCity ile Selenium

### Bölüm 7 — Bitiş
- [ ] **Selenium Quiz** çöz
- [ ] Sertifikayı al → LinkedIn'de paylaş
- [ ] Repoyu GitHub'a at, README'yi cilala

---

## 📓 Ders Notlarım

### Ders 1 — Development Setup (Python) ✅
**Tarih:** 2026-07-22

**Öğrendiklerim:**
- Selenium testleri için gereken: Python + bir IDE + bir unit test framework'ü.
  Eğitim PyUnit (unittest) örnekleri veriyor ama başka framework de olur —
  biz modern ve yaygın olduğu için **pytest** seçtik.
- **Sanal ortam (venv):** proje bağımlılıklarını sistemden ayrı tutar. Her
  projenin kendi paket seti olur, sürüm çakışması yaşamazsın.
- **Selenium Manager:** Selenium 4.6+ ile geliyor. Doğru `chromedriver`'ı
  otomatik indiriyor — artık elle driver indirmeye gerek yok.
- **fixture (conftest.py):** tekrar eden kurulum kodunu (tarayıcı aç/kapat)
  tek yerde toplama yöntemi. `driver` fixture'ını her teste parametre olarak
  veriyoruz.

**Kurduğumuz araçlar:** Python 3.12 · selenium 4.46 · pytest 9.1 · webdriver-manager

**Kanıt kod:** `tests/ders_01_kurulum/test_kurulum.py` — 2 test, ikisi de geçti.

> **Not (kendime):** PyUnit ile pytest farkı — PyUnit'te `class Test(unittest.TestCase)`
> ve `self.assertEqual(...)` yazarsın; pytest'te düz fonksiyon + sade `assert`
> yeterli. İkisi de aynı işi yapar, pytest daha az kod.

---

### Ders 2 — İlk WebDriver Etkileşimi (Locator'lar) ✅
**Tarih:** 2026-07-22

**Öğrendiklerim:**
- Her Selenium testinin 3 adımı var: **Bul (locator) → Aksiyon uygula → Doğrula (assert)**.
- **Locator türleri** (`from selenium.webdriver.common.by import By`):
  | Locator | Ne zaman | Örnek |
  |---------|----------|-------|
  | `By.ID` | En güvenilir, ilk tercih | `find_element(By.ID, "username")` |
  | `By.NAME` | id yoksa | `By.NAME, "q"` |
  | `By.LINK_TEXT` | Linkin görünen metni | `By.LINK_TEXT, "Form Authentication"` |
  | `By.CSS_SELECTOR` | Esnek ve hızlı | `By.CSS_SELECTOR, "button[type='submit']"` |
  | `By.XPATH` | En esnek ama kırılgan | `By.XPATH, "//h2[text()='Login']"` |
  | `By.TAG_NAME` | Etiket adı | `By.TAG_NAME, "h2"` |
- **Aksiyonlar:** `.click()` (tıkla), `.send_keys("metin")` (yaz), `.text` (metni oku).
- **Kural:** Mümkünse `id` kullan. `xpath`'i en son çare olarak kullan (sayfa
  değişince kolay kırılır → *flaky test* riski, ileride o dersi işleyeceğiz).

**Kanıt kod:** `tests/ders_02_locators/test_locators.py` — 3 test (link tıklama,
başarılı giriş, hatalı giriş), üçü de geçti.

> **Satış notu (kendime):** Müşteriye şöyle anlatılır → "Bir kullanıcının login
> olması, yanlış şifrede uyarı görmesi gibi senaryoları saniyeler içinde,
> otomatik ve her sürümde tekrar test edebiliyoruz. Manuel test saatlerini
> dakikaya indiriyoruz."

---

### Ders 3 — Selenium WebDrivers Explained ✅
**Tarih:** 2026-07-25

**Öğrendiklerim:**
- **WebDriver nedir?** Selenium'un tarayıcıya emir vermesini sağlayan aracı
  program. Her tarayıcının kendi sürücüsü var:

  | Tarayıcı | Sürücü | Python sınıfı |
  |----------|--------|---------------|
  | Chrome | chromedriver | `webdriver.Chrome()` |
  | Edge | msedgedriver | `webdriver.Edge()` |
  | Firefox | geckodriver | `webdriver.Firefox()` |
  | Safari (macOS) | safaridriver | `webdriver.Safari()` |
  | Uzak makine / Grid | — | `webdriver.Remote()` |

- **Önemli kavrayış:** Sürücü ve Options sınıfı tarayıcıya göre değişir, ama
  driver nesnesini bir kere aldıktan sonra **API tamamen aynı**. `get()`,
  `find_element()`, `click()` her tarayıcıda birebir aynı yazılır. Cross-browser
  testin mümkün olmasının sebebi bu.
- **Options (capabilities):** Tarayıcı açılmadan ÖNCE verdiğimiz ayarlar —
  `--start-maximized`, `--disable-notifications`, `--window-size=1920,1080`.
  Headless argümanı bile tarayıcıya göre değişiyor:
  Chrome/Edge → `--headless=new`, Firefox → `-headless` (tek tire!).
- **Headless mod:** Tarayıcı arayüzü ekranda görünmeden çalışır. Ekranı olmayan
  CI sunucularında (Jenkins, GitHub Actions) şart. Ayrıca çok daha hızlı.
- **`quit()` vs `close()`:** `close()` sadece aktif sekmeyi kapatır ve
  chromedriver.exe arkada asılı kalabilir; `quit()` her şeyi sonlandırır.
  **Test sonunda her zaman `quit()`.**
- **Selenium Manager** (4.6+) bu sürücülerin hepsini otomatik indiriyor —
  elle indirme/PATH'e ekleme derdi bitti.

**conftest.py'de yaptığımız değişiklik:**
- `driver` fixture'ı artık Chrome'a sabit değil, komut satırından seçiliyor.
- Tek testte birden fazla tarayıcı açabilmek için `driver_fabrikasi` fixture'ı
  eklendi (cross-browser testleri bunu kullanıyor).

```powershell
pytest                       # varsayılan: chrome
pytest --browser=edge        # Edge ile çalıştır
pytest --browser=firefox     # Firefox ile (kuruluysa)
pytest --headless            # tarayıcıyı gizle (CI modu)
pytest -m crossbrowser       # sadece cross-browser testleri
```

**Kanıt kod:** `tests/ders_03_webdrivers/test_webdrivers.py` — 6 test, hepsi geçti.
Cross-browser testi bu makinede kurulu tarayıcıları otomatik bulup her birinde
aynı login senaryosunu koşturuyor (Chrome ✅ + Edge ✅; Firefox kurulu değil,
kurulursa otomatik dahil olur).

**Tüm suite:** 11 test, `pytest --headless` ile hepsi yeşil.

> **Satış notu (kendime):** Müşteriye şöyle anlatılır → "Sitenizi Chrome'da test
> ettik diye Edge'de de çalışıyor demek değil. Aynı senaryoyu tek komutla tüm
> tarayıcılarda koşturuyoruz; 'bende çalışıyordu' tartışması bitiyor. Üstelik
> headless modda sunucuda, geceleri, kimse başında olmadan çalışıyor."

---

### Ders 4 — (bir sonraki dersi işleyince yazacağım)
**Tarih:**

**Öğrendiklerim:**
-

**Kanıt kod:**

---

## 💡 Fikir Havuzu (proje ilerledikçe eklenecek)

Bu bölüm senin isteğinle: aklıma yeni fikir geldikçe buraya ekliyorum.

- **Demo hedef site:** Gerçek sitelere değil, otomasyon için yapılmış güvenli
  test sitelerine karşı çalış: `the-internet.herokuapp.com`, `saucedemo.com`,
  `demoqa.com`. (Gerçek prod sitelerinde otomasyon hem kırılgan hem etik/yasal
  açıdan riskli.)
- **Satış tarafı için köprü:** Her dersin sonuna "Bunu müşteriye nasıl
  anlatırım?" diye 1-2 cümlelik iş değeri notu ekle. Teknik + satış birleşimi
  seni ayrıştırır.
- **HTML rapor:** İleride `pytest-html` ekleyip güzel test raporu üretebiliriz
  (LinkedIn/GitHub'da göstermek için görsel malzeme).
- **CI otomasyonu:** Repo GitHub'a gidince GitHub Actions ile her push'ta
  testleri otomatik çalıştırırız — CV'de "CI/CD" maddesi olur.
- **Page Object Model klasörü:** `pages/` klasörü POM dersinde devreye girecek.
- **Sertifika kanıtı:** Sertifikayı alınca `docs/` altına ekle, README'de göster.

---

## 🐙 Git / GitHub Akışı

✅ **Repo kuruldu ve GitHub'a yüklendi** (2026-07-25).
Adres: <https://github.com/anllkvk/selenium.academy>
Branch: `main` · Bundan sonrası her ders için bir commit.

Her dersten sonra:
```powershell
git add .
git commit -m "Ders X: <ne öğrendim>"
git push
```
> İyi commit mesajı = ilerlemenin görünür kanıtı. İşe alımcı repoya bakınca
> düzenli çalıştığını görür.
