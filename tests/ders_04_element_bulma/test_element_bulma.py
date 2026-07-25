"""
Ders 4 — Element Identification (Elementleri Tanımlama)

Dersin üç başlığı vardı: Finding Elements / Static Elements / Dynamic Elements.
Bu dosya o üç başlığı sırayla, çalışan kodla gösteriyor.

TEMEL FİKİR:
    Selenium sayfayı senin gibi "görmez". Ona "şu butona bas" diyemezsin;
    "şu ADRESTEKİ elemente bas" demen gerekir. Locator = elementin adresi.
    Elementi bulamazsa hiçbir şey yapamaz. O yüzden işin %80'i locator yazmak.

STATİK vs DİNAMİK (dersin can alıcı noktası):
    Statik element  -> id/name'i her açılışta AYNI kalır. Kolay iş: By.ID yeter.
    Dinamik element -> id'si her sayfa yüklemesinde DEĞİŞİR
                       (örn. React/Angular'ın ürettiği id'ler, oturum numaraları).
                       Bunlara id ile locator yazarsan test yarın patlar.
                       Çözüm: değişmeyen bir şeye tutun (class, etiket yapısı,
                       metin, data-* attribute) veya kısmi eşleşme kullan.

Çalıştır:
    pytest tests/ders_04_element_bulma -v -s
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

ANA_SAYFA = "https://the-internet.herokuapp.com/"
ZOR_DOM = ANA_SAYFA + "challenging_dom"      # id'leri her yüklemede değişen sayfa
DINAMIK_KONTROL = ANA_SAYFA + "dynamic_controls"  # elementleri sonradan gelen sayfa


# ---------------------------------------------------------------------------
# 1) FINDING ELEMENTS — tekil mi, çoğul mu?
# ---------------------------------------------------------------------------

@pytest.mark.elementler
@pytest.mark.smoke
def test_find_element_ile_find_elements_farki(driver):
    """
    find_element  (tekil) -> İLK eşleşeni döndürür. Bulamazsa HATA fırlatır.
    find_elements (çoğul) -> LİSTE döndürür. Bulamazsa BOŞ liste döner, hata yok.

    Kural: "var mı yok mu?" diye kontrol edeceksen çoğulunu kullan,
    çünkü tekili bulamayınca testi patlatır.
    """
    driver.get(ANA_SAYFA)

    # Tekil: sayfadaki ilk başlık
    baslik = driver.find_element(By.TAG_NAME, "h1")
    assert baslik.text == "Welcome to the-internet"

    # Çoğul: sayfadaki TÜM linkler
    linkler = driver.find_elements(By.CSS_SELECTOR, "ul li a")
    assert len(linkler) > 30  # bu demo sitede 40+ örnek sayfa var
    print(f"\n[OK] Sayfada {len(linkler)} adet örnek linki bulundu.")

    # Olmayan bir şeyi çoğul ile aramak GÜVENLİ: boş liste döner
    olmayanlar = driver.find_elements(By.ID, "boyle-bir-id-yok")
    assert olmayanlar == []
    print("[OK] Olmayan element çoğul aramada boş liste döndürdü (hata vermedi).")


@pytest.mark.elementler
def test_bulunamayan_element_hata_firlatir(driver):
    """
    Tekil arama bulamazsa NoSuchElementException fırlatır.
    Bu Selenium'da en sık gördüğün hatadır; sebebi genelde şu üçünden biri:
      1. Locator yanlış yazılmış
      2. Element henüz yüklenmemiş (bekleme sorunu -> bir sonraki ders)
      3. Element iframe içinde veya gerçekten sayfada yok
    """
    driver.get(ANA_SAYFA)

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, "boyle-bir-id-yok")

    print("\n[OK] Olmayan element tekil aramada beklendiği gibi hata fırlattı.")


# ---------------------------------------------------------------------------
# 2) STATIC ELEMENTS — id'si değişmeyen elementler
# ---------------------------------------------------------------------------

@pytest.mark.elementler
def test_statik_elementler_id_ile_bulunur(driver):
    """
    Login formundaki alanların id'si her açılışta aynı: 'username', 'password'.
    Bunlar STATİK element. En kolay ve en sağlam locator: By.ID.
    """
    driver.get(ANA_SAYFA + "login")

    # Aynı sayfayı iki kez açıp id'lerin değişmediğini kanıtlıyoruz
    ilk = driver.find_element(By.ID, "username").get_attribute("id")
    driver.refresh()
    ikinci = driver.find_element(By.ID, "username").get_attribute("id")

    assert ilk == ikinci == "username"
    print(f"\n[OK] Statik element: id iki yüklemede de '{ilk}' kaldı.")


@pytest.mark.elementler
def test_ayni_elemente_farkli_locator_yollari(driver):
    """
    Bir elemente birden fazla adresle ulaşabilirsin. Hepsi AYNI elementi bulur.
    Amaç: locator yazmanın "tek doğrusu" olmadığını, seçenekleri görmek.
    """
    driver.get(ANA_SAYFA + "login")

    yollar = {
        "By.ID":            (By.ID, "username"),
        "By.NAME":          (By.NAME, "username"),
        "By.CSS (id ile)":  (By.CSS_SELECTOR, "#username"),
        "By.CSS (attr)":    (By.CSS_SELECTOR, "input[name='username']"),
        "By.XPATH (attr)":  (By.XPATH, "//input[@id='username']"),
        "By.XPATH (yapı)":  (By.XPATH, "//form[@id='login']//input[1]"),
    }

    # Her locator'ın bulduğu elementin Selenium içindeki kimliği aynı olmalı
    kimlikler = set()
    for isim, (nasil, ne) in yollar.items():
        el = driver.find_element(nasil, ne)
        kimlikler.add(el.id)  # Selenium'un elemente verdiği iç kimlik
        print(f"\n  {isim:18} -> bulundu")

    assert len(kimlikler) == 1, "Tüm locator'lar aynı elementi bulmalıydı"
    print("\n[OK] 6 farklı locator da aynı input elementini buldu.")


# ---------------------------------------------------------------------------
# 3) DYNAMIC ELEMENTS — id'si her yüklemede değişen elementler
# ---------------------------------------------------------------------------

@pytest.mark.elementler
def test_dinamik_id_kanitla_ve_id_kullanma(driver):
    """
    KANIT: challenging_dom sayfasındaki butonların id'si her yüklemede değişiyor.
    Bu yüzden By.ID kullanmak burada ölümcül hata olur — test yarın kırılır.
    """
    driver.get(ZOR_DOM)
    ilk_idler = [b.get_attribute("id") for b in driver.find_elements(By.CSS_SELECTOR, "a.button")]

    driver.refresh()
    ikinci_idler = [b.get_attribute("id") for b in driver.find_elements(By.CSS_SELECTOR, "a.button")]

    print(f"\n  1. yükleme id: {ilk_idler[0]}")
    print(f"  2. yükleme id: {ikinci_idler[0]}")

    assert ilk_idler != ikinci_idler, "Bu sayfada id'ler değişmeliydi"
    print("[OK] id'ler değişti -> bu elementler DİNAMİK. By.ID kullanılamaz.")


@pytest.mark.elementler
def test_dinamik_elementi_degismeyen_ozellikle_bul(driver):
    """
    id değişiyor ama CLASS değişmiyor. Çözüm: değişmeyene tutun.

    Not: bu sayfada butonların METNİ de rastgele değişiyor (foo/bar/baz),
    o yüzden metne göre locator da güvenilmez. Sağlam olan: class + sıra.
    """
    driver.get(ZOR_DOM)

    # Üç butonun class'ları sabit: 'button', 'button alert', 'button success'
    normal = driver.find_element(By.CSS_SELECTOR, "a.button:not(.alert):not(.success)")
    uyari = driver.find_element(By.CSS_SELECTOR, "a.button.alert")
    basari = driver.find_element(By.CSS_SELECTOR, "a.button.success")

    for isim, el in (("normal", normal), ("alert", uyari), ("success", basari)):
        assert el.is_displayed()
        print(f"\n  {isim:8} buton -> class='{el.get_attribute('class')}' (id: değişken)")

    # Aynısını XPath ile: contains() kısmi eşleşme yapar
    uyari_xpath = driver.find_element(By.XPATH, "//a[contains(@class, 'alert')]")
    assert uyari_xpath.id == uyari.id
    print("\n[OK] CSS ve XPath ile aynı dinamik buton bulundu (id'ye dokunmadan).")


@pytest.mark.elementler
def test_kismi_eslesme_operatorleri(driver):
    """
    Dinamik id'lerle çalışmanın diğer yolu: KISMİ EŞLEŞME.

    CSS'te:   [id^='ab']  başlayan     [id$='yz']  biten     [id*='cd']  içeren
    XPath'te: starts-with(@id,'ab')    contains(@id,'cd')

    Gerçek hayatta id'ler genelde 'user_input_8fa2b' gibi
    'sabit-önek + rastgele-son' şeklinde olur; işte o zaman ^= hayat kurtarır.
    """
    driver.get(ANA_SAYFA + "login")

    # 'username' id'sini kısmi eşleşmeyle bulalım
    bastan = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")     # ile başlayan
    sondan = driver.find_element(By.CSS_SELECTOR, "input[id$='name']")     # ile biten
    iceren = driver.find_element(By.CSS_SELECTOR, "input[id*='sernam']")   # içeren
    xpath_bastan = driver.find_element(By.XPATH, "//input[starts-with(@id, 'user')]")

    kimlikler = {bastan.id, sondan.id, iceren.id, xpath_bastan.id}
    assert len(kimlikler) == 1
    print("\n[OK] ^= $= *= ve starts-with() dördü de aynı elementi buldu.")


@pytest.mark.elementler
def test_tabloda_satir_bul_ve_o_satirda_islem_yap(driver):
    """
    GERÇEK HAYAT SENARYOSU (en sık ihtiyaç duyacağın kalıp):
    "Tabloda 'X' yazan satırı bul, O SATIRDAKİ edit linkine tıkla."

    Buradaki püf nokta: önce metinden satırı buluyoruz, sonra o satırın
    içinde arama yapıyoruz. Elementin kendi üzerinden find_element çağırınca
    arama sadece o elementin İÇİNDE yapılır.
    """
    driver.get(ZOR_DOM)

    # 1. yol: XPath ile "içinde 'Iuvaret1' yazan hücre olan satır"
    satir = driver.find_element(By.XPATH, "//tr[td[text()='Iuvaret1']]")
    hucreler = [td.text for td in satir.find_elements(By.TAG_NAME, "td")]
    print(f"\n  Bulunan satır: {hucreler[:3]} ...")
    assert hucreler[0] == "Iuvaret1"

    # 2. Satırın İÇİNDE 'edit' linkini ara (nokta '.' = 'bu elementin içinde')
    edit_linki = satir.find_element(By.LINK_TEXT, "edit")
    edit_linki.click()

    assert "#edit" in driver.current_url
    print(f"[OK] Doğru satırın edit linkine tıklandı -> {driver.current_url}")


@pytest.mark.elementler
def test_sonradan_ortaya_cikan_element(driver):
    """
    "Dinamik" kelimesinin ikinci anlamı: element sayfada SONRADAN belirir/kaybolur.

    Burada 'Remove' butonuna basınca checkbox siliniyor ve yerine mesaj çıkıyor.
    Mesaj hemen gelmiyor (~2 sn). conftest.py'deki implicitly_wait(5) sayesinde
    Selenium 5 saniyeye kadar bekliyor.

    -> Beklemenin doğru yolu (explicit wait) bir sonraki dersin konusu.
    """
    driver.get(DINAMIK_KONTROL)

    # Başlangıçta checkbox VAR
    assert len(driver.find_elements(By.CSS_SELECTOR, "#checkbox")) == 1

    driver.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()

    # Mesaj sonradan belirir — implicit wait bunu bekler
    mesaj = driver.find_element(By.ID, "message").text
    assert "gone" in mesaj.lower()

    # Artık checkbox YOK (çoğul arama ile güvenli kontrol)
    assert driver.find_elements(By.CSS_SELECTOR, "#checkbox") == []
    print(f"\n[OK] Element silindi, mesaj geldi: '{mesaj}'")


# ---------------------------------------------------------------------------
# 📌 DERS NOTU — Locator seçme sırası (yukarıdan aşağıya dene)
#
#   1. id                       -> varsa ve SABİTSE her zaman birinci tercih
#   2. name / data-testid       -> data-* attribute'ları test için konur, çok sağlam
#   3. CSS selector             -> hızlı, okunabilir; class + attribute kombinasyonu
#   4. link text                -> sadece <a> etiketleri için, metin sabitse
#   5. XPath                    -> en güçlü (metne göre arama, yukarı çıkma) ama
#                                  en kırılgan; son çare olarak kullan
#
#   ASLA yapma: mutlak XPath  (/html/body/div[2]/div/div[1]/form/input[3])
#   Sayfada tek bir <div> eklenince kırılır. Hiçbir test buna dayanamaz.
# ---------------------------------------------------------------------------
