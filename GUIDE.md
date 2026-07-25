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
   → **Ders 6'dan itibaren:** test dosyası bana **boşluklu** geliyor. Kritik
   2-3 satır `# TODO(anıl):` olarak boş bırakılıyor, onları ben dolduruyorum.
   Takılırsam cevabı soruyorum. *(Amaç: pasif okuyucu değil, yazan olmak.)*
5. `pytest` ile çalıştır, yeşil olduğunu gör.
6. Anlamlı bir commit at (aşağıdaki git bölümüne bak).

> 📎 **HTML'i unuttuysan / hiç bilmiyorsan:** en alttaki
> [Ek: Selenium için gereken kadar HTML](#-ek-selenium-için-gereken-kadar-html)
> bölümünü oku. Selenium'un sisli gelmesinin sebebi genelde Selenium değil,
> HTML boşluğudur.

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
- [x] **Element Identification** — statik/dinamik elementler, kısmi eşleşme ✅ *(ders_04_element_bulma/test_element_bulma.py)*
- [x] **Element Interaction** — tıklama, yazma, checkbox, dropdown ✅ *(ders_05_etkilesim/test_etkilesim.py)*
- [ ] Bekleme (wait) türleri: implicit / explicit ← **sıradaki**

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

### Ders 4 — Element Identification (Elementleri Tanımlama) ✅
**Tarih:** 2026-07-25
**Kaynak:** [Ders sayfası](https://selenium.academy/selenium-identifying-elements/) ·
[Yazılı hali](https://selenium.academy/selenium-identifying-elements-text-version/)

Dersin üç başlığı: **Finding Elements / Static Elements / Dynamic Elements**.

**Temel fikir (kendi cümlemle):**
Selenium sayfayı benim gibi görmüyor. "Şu butona bas" diyemiyorum, "şu
ADRESTEKİ elemente bas" dememem gerekiyor. **Locator = elementin adresi.**
Elementi bulamazsa hiçbir şey yapamaz — o yüzden bu işin büyük kısmı
locator yazmak.

**1) Finding Elements — tekil vs çoğul**

| | Bulursa | Bulamazsa |
|---|---------|-----------|
| `find_element` (tekil) | İLK eşleşeni verir | `NoSuchElementException` **fırlatır** |
| `find_elements` (çoğul) | Liste verir | **Boş liste** döner, hata yok |

> Kural: "var mı yok mu?" kontrolü yapacaksam çoğulunu kullanmalıyım.

**2) Static Elements** — `id`/`name`'i her açılışta aynı kalan elementler.
İşin kolay tarafı: `By.ID` yeter. (Login formundaki `username`, `password` gibi.)

**3) Dynamic Elements** — dersin can alıcı noktası. İki ayrı anlamı var:
- **a) id'si her yüklemede değişen elementler.** React/Angular'ın ürettiği
  id'ler, oturum numaraları... Bunlara `By.ID` yazarsam testim yarın kırılır.
  *Kanıtladım:* `challenging_dom` sayfasındaki butonun id'si iki yüklemede
  `cf620bd0-...` → `d03e6840-...` oldu. **Çözüm: değişmeyene tutun** (class,
  yapı, data-* attribute) veya **kısmi eşleşme** kullan.
- **b) Sayfada sonradan beliren/kaybolan elementler.** Butona basınca 2 saniye
  sonra gelen mesaj gibi. Şimdilik `implicitly_wait(5)` kurtarıyor;
  doğru çözüm **explicit wait** → bir sonraki ders.

**Kısmi eşleşme operatörleri (dinamik id'lerin ilacı):**

| İstediğim | CSS | XPath |
|-----------|-----|-------|
| ile başlayan | `input[id^='user']` | `starts-with(@id,'user')` |
| ile biten | `input[id$='name']` | — |
| içeren | `input[id*='sernam']` | `contains(@id,'sernam')` |

> Gerçek hayatta id'ler `user_input_8fa2b` gibi *sabit önek + rastgele son*
> şeklinde olur; işte o zaman `^=` hayat kurtarır.

**Locator seçme sırası (yukarıdan aşağı dene):**
1. `id` — varsa ve **sabitse** her zaman birinci tercih
2. `name` / `data-testid` — data-* attribute'ları zaten test için konur, çok sağlam
3. **CSS selector** — hızlı, okunabilir (XPath'ten hızlı çalışır)
4. `link text` — sadece `<a>` için, metin sabitse
5. **XPath** — en güçlü (metne göre arama, yukarı çıkma) ama en kırılgan, son çare

> ❌ **Asla:** mutlak XPath (`/html/body/div[2]/div/div[1]/form/input[3]`).
> Sayfaya tek bir `<div>` eklenince kırılır.

**En çok işime yarayacak kalıp — tabloda satır bulup o satırda işlem:**
```python
satir = driver.find_element(By.XPATH, "//tr[td[text()='Iuvaret1']]")
satir.find_element(By.LINK_TEXT, "edit").click()   # arama SADECE o satırın içinde
```
Bir elementin üzerinden `find_element` çağırınca arama o elementin **içinde**
yapılıyor. Bu, "doğru satırın butonuna basma" problemini çözüyor.

**Kanıt kod:** `tests/ders_04_element_bulma/test_element_bulma.py` — 9 test, hepsi geçti.

> **Satış notu (kendime):** Müşteriye → "Testlerin neden bazen kendiliğinden
> bozulduğunu biliyor musunuz? Çoğu zaman sayfadaki elementlerin kimliği her
> açılışta değiştiği içindir. Biz testleri değişmeyen özelliklere bağlayarak
> yazıyoruz; siteniz güncellendiğinde testler ayakta kalıyor."

---

### Ders 5 — Element Interaction (Elementlerle Etkileşim) ✅
**Tarih:** 2026-07-26
**Kaynak:** [Ders sayfası](https://selenium.academy/selenium-element-interaction/)

**Ders notum:** Selenium kullanarak sayfa elemanlarıyla nasıl etkileşim
kurarız — dersin dört başlığı: **Clicking / Text input / Checkbox / ComboBox**.

**Önceki derse bağlantısı:** Ders 4 "elementi nasıl BULURUM" idi, bu ders
"bulduktan sonra NE YAPARIM". Selenium'un tamamı aslında bu iki adım:
**bul → etkileşime gir.**

**1) Clicking** — `click()`. Kritik nokta: tıklama sayfayı **değiştirir**.
Tıkladıktan sonra elementleri **yeniden sorgulamak** gerekir, eski listeyle
devam edilemez.

**2) Text input** — `send_keys()` yazıyı **ekler**, üzerine yazmaz.
Var olan değeri değiştireceksem önce `clear()`.
> `anilkavak` gibi birbirine yapışmış değerler hep bu yüzden oluşuyor.

**3) Checkbox** — `click()` bir anahtar değil **toggle**. İşaretliyse kaldırır.
Doğru yöntem "tıkla" demek değil, **"şu duruma getir"** demek:
```python
if kutu.is_selected() != istenen_durum:
    kutu.click()
```

**4) ComboBox** — `<select>` için özel yardımcı: **`Select` sınıfı**.
`select_by_visible_text()` / `select_by_value()` / `select_by_index()`.
Tercihim visible_text: sayfa değişince en az kırılan ve testi okuyan kişi
ne seçildiğini anlıyor.

**Takıldığım/öğrendiğim iki kritik ayrım:**

| | Ne verir | Ne zaman |
|---|---|---|
| `.text` | Etiketin **arasındaki** yazı | `<h2>Login Page</h2>` |
| `.get_attribute("value")` | Input'un **içindeki** değer | `<input value="tomsmith">` |

> Input'a `.text` dersem **boş string** alırım. "Neden çalışmıyor" krizlerinin
> klasik sebebi bu.

| Metot | Sorusu |
|---|---|
| `is_displayed()` | Ekranda görünüyor mu? |
| `is_enabled()` | Aktif/tıklanabilir mi? (gri değil mi) |
| `is_selected()` | İşaretli mi? (sadece checkbox/radio) |

**Etkileşim komutları özeti:**
`click()` · `send_keys("yazı")` · `send_keys(Keys.RETURN)` · `clear()` ·
`submit()` · `.text` · `get_attribute("value")` · `is_displayed()` ·
`is_enabled()` · `is_selected()` · `Select(el)`

**Kanıt kod:** `tests/ders_05_etkilesim/test_etkilesim.py` — 9 test, hepsi geçti.
Testlerin ikisi bilinçli olarak **tuzağı gösteriyor**: `clear()` olmadan yazınca
değerlerin yapışması ve checkbox'a körlemesine tıklayınca durumun ters dönmesi.

> **Satış notu (kendime):** Müşteriye → "Bir kullanıcının yapabildiği her şeyi
> otomatik yapabiliyoruz: form doldurma, kutucuk işaretleme, liste seçimi.
> Sipariş formunuzun 20 farklı kombinasyonunu her sürümde dakikalar içinde
> deniyoruz — manuel olarak kimsenin yapmaya vakti olmayan şey bu."

---

### Ders 6 — (bir sonraki dersi işleyince yazacağım)
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
- ~~**CI otomasyonu:**~~ ✅ **Yapıldı (2026-07-25).** GitHub Actions her push'ta
  testleri Ubuntu sunucusunda Chrome + Edge ile headless çalıştırıyor
  (`.github/workflows/tests.yml`). README'de yeşil/kırmızı rozet var.
  CV/LinkedIn'de "CI/CD (GitHub Actions)" maddesi artık gerçek bir kanıta dayanıyor.
  *Not: Bölüm 6'daki Jenkins/TeamCity derslerini işlerken bu deneyim işine yarayacak.*
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

---

## 📎 Ek: Selenium için gereken kadar HTML

> Bu bölümü 2026-07-26'da ekledim. Sebebi: dersleri izlerken "teknik bilgim
> eksik" hissi veren şey Selenium değil, **HTML boşluğuydu.** Selenium'un tek
> yaptığı şey HTML'deki bir düğüme dokunmak — HTML'i görünce Selenium
> kendiliğinden anlaşılıyor. Buraya *sadece Selenium için gereken kadarını*
> yazdım, 10 dakikada okunur.

### 1. Bir web sayfası aslında nedir?

Tarayıcının indirdiği şey bir **metin dosyası**: HTML. İçinde iç içe geçmiş
**etiketler** (tag) var. Tarayıcı bu metni okuyup ekrana çiziyor.

```html
<h2>Login Page</h2>
<input type="text" id="username" name="username" class="form-input">
<button type="submit">Login</button>
```

Sen ekranda "Login yazan mavi buton" görüyorsun; Selenium ise
`<button type="submit">` satırını görüyor. **İkisi aynı şey.**

### 2. Etiket anatomisi (buradaki 4 kelimeyi bilmek yeter)

```
<input type="text" id="username" class="form-input">  ...  </input>
 └─┬─┘ └──────────────┬──────────────────────────┘
   │                  │
ETİKET ADI        ATTRIBUTE'LAR (özellikler)
(tag name)        her biri  isim="değer"  şeklinde
```

| Terim | Ne demek | Selenium'daki karşılığı |
|-------|----------|--------------------------|
| **etiket adı** | Elementin türü: `input`, `button`, `a`, `h2`, `tr`, `td` | `By.TAG_NAME` |
| **attribute** | Etikete yazılan `isim="değer"` çiftleri | `get_attribute("...")` |
| **id** | Sayfada **tek** olması gereken kimlik | `By.ID` ← ilk tercih |
| **class** | **Birden fazla** elementte olabilen etiket/grup | `By.CLASS_NAME`, CSS `.sinif` |
| **text** | Etiketin **arasındaki** yazı: `<h2>BURASI</h2>` | `.text` |

> 🔑 **id vs class:** id = TC kimlik numarası (tek kişide olur).
> class = meslek (aynı meslekten yüzlerce kişi olabilir).
> Bu yüzden id ile ararsan 1 element, class ile ararsan liste dönme ihtimali var.

### 3. DOM ağacı — "içinde/içinde" mantığı

Etiketler iç içe geçer. Bu iç içe yapıya **DOM ağacı** denir:

```html
<form id="login">                 <!-- ana kutu (parent) -->
  <div class="row">               <!--   içindeki kutu -->
    <label for="username">Username</label>
    <input id="username">         <!--     en içteki element (child) -->
  </div>
</form>
```

Bu yüzden Ders 4'teki şu kalıp çalışıyor:
```python
satir = driver.find_element(By.XPATH, "//tr[td[text()='Iuvaret1']]")
satir.find_element(By.LINK_TEXT, "edit").click()   # arama sadece o satırın İÇİNDE
```
Önce büyük kutuyu buluyorum, sonra **onun içinde** arıyorum. Tablolarda
"doğru satırın butonuna basma" problemi böyle çözülüyor.

### 4. Form elementleri (Ders 5'in tamamı bu)

| HTML | Ne görünür | Selenium'da |
|------|-----------|-------------|
| `<input type="text">` | Yazı kutusu | `send_keys()`, `clear()`, `get_attribute("value")` |
| `<input type="checkbox">` | Kutucuk | `click()`, `is_selected()` |
| `<input type="radio">` | Yuvarlak seçenek | `click()`, `is_selected()` |
| `<button>` | Buton | `click()` |
| `<a href="...">` | Link | `click()`, `By.LINK_TEXT` |
| `<select>` + `<option>` | Açılır liste | `Select(el).select_by_visible_text()` |
| `<label>` | Alanın yanındaki yazı | genelde sadece okunur |

**Açılır listenin gerçek hali:**
```html
<select id="dropdown">
  <option value="" disabled selected>Please select an option</option>
  <option value="1">Option 1</option>     <!-- value=makine için, "Option 1"=insan için -->
  <option value="2">Option 2</option>
</select>
```
`select_by_value("1")` → makine tarafını, `select_by_visible_text("Option 1")`
→ insan tarafını kullanır. İkisi aynı seçeneği seçer.

### 5. `.text` vs `value` — neden ikisi farklı?

```html
<h2>Login Page</h2>              <!-- yazı etiketin ARASINDA  -> .text -->
<input id="username" value="">   <!-- yazı bir ATTRIBUTE'ta   -> get_attribute("value") -->
```
Kullanıcı input'a yazı yazdığında HTML kaynağı değişmez, elementin `value`'su
değişir. Bu yüzden input'a `.text` dersen **boş string** alırsın.

### 6. Tarayıcıda canlı görmek (en öğretici kısım)

Herhangi bir sayfada **F12** → **Elements** sekmesi → bir öğeye sağ tık →
**Inspect**. Ekranda gördüğün şeyin HTML karşılığı hemen vurgulanır.

**Console** sekmesinde locator'ı Selenium'a yazmadan önce dene:
```javascript
$$("a.button")                     // CSS: kaç element eşleşti?
$$("input[id^='user']")            // kısmi eşleşme tutuyor mu?
$x("//tr[td[text()='Iuvaret1']]")  // XPath: doğru satırı buldu mu?
```
> Kural: **Selenium'a yazmadan önce konsolda test et.** En çok zaman
> kazandıracak alışkanlık bu.

### 7. Daha fazlası için

- [MDN — HTML'e giriş (Türkçe)](https://developer.mozilla.org/tr/docs/Learn_web_development/Core/Structuring_content)
- [W3Schools — HTML Forms](https://www.w3schools.com/html/html_forms.asp) (input/select/checkbox — bizim konumuz)
- [MDN — CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)
