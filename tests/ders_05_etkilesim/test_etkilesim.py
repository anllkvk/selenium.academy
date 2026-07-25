"""
Ders 5 — Element Interaction (Elementlerle Etkileşim)

Dersin dört başlığı vardı ve bu dosya tam olarak o sırayı takip ediyor:
    1. Clicking Elements   -> tıklama
    2. Text input          -> yazı yazma
    3. Selecting a Checkbox-> kutucuk işaretleme
    4. Using a ComboBox    -> açılır liste (dropdown) seçimi

ÖNCEKİ DERSLE BAĞLANTISI:
    Ders 4 "elementi NASIL BULURUM" idi. Bu ders "bulduktan sonra NE YAPARIM".
    Selenium'un tamamı aslında bu iki adım:  bul  ->  etkileşime gir.

Çalıştır:
    pytest tests/ders_05_etkilesim -v -s
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

B = "https://the-internet.herokuapp.com/"


# ---------------------------------------------------------------------------
# 1) CLICKING ELEMENTS — tıklama
# ---------------------------------------------------------------------------

@pytest.mark.etkilesim
@pytest.mark.smoke
def test_tiklama_ile_element_ekle_ve_sil(driver):
    """
    'Add Element' butonuna her basışta sayfaya yeni bir 'Delete' butonu ekleniyor.

    Buradaki ders: tıklama sayfayı DEĞİŞTİRİR. Tıkladıktan sonra sayfanın
    yeni halini yeniden sorgulamak gerekir — eski listeyi kullanmaya devam edemezsin.
    """
    driver.get(B + "add_remove_elements/")

    ekle_butonu = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")

    # Başlangıçta hiç Delete butonu yok
    assert driver.find_elements(By.CSS_SELECTOR, ".added-manually") == []

    # Üç kez tıkla -> üç Delete butonu oluşmalı
    for _ in range(3):
        ekle_butonu.click()

    silme_butonlari = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(silme_butonlari) == 3
    print(f"\n[OK] 3 tıklama -> {len(silme_butonlari)} adet Delete butonu oluştu.")

    # Bir tanesine tıklayıp silelim
    silme_butonlari[0].click()

    # DİKKAT: listeyi YENİDEN sorguluyoruz. Eski liste artık güncel değil.
    kalan = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(kalan) == 2
    print(f"[OK] 1 silme -> {len(kalan)} buton kaldı.")


@pytest.mark.etkilesim
def test_element_durumlari_displayed_enabled_selected(driver):
    """
    Tıklamadan ÖNCE elementin durumunu sorabilirsin. Üçü farklı şeydir:

        is_displayed() -> ekranda görünüyor mu?      (gizli mi değil mi)
        is_enabled()   -> tıklanabilir/aktif mi?     (gri/pasif mi değil mi)
        is_selected()  -> işaretli mi?               (SADECE checkbox/radio için)

    Pasif (disabled) bir elemente tıklamaya çalışmak testi patlatır;
    önce is_enabled() ile sormak iyi alışkanlıktır.
    """
    driver.get(B + "dynamic_controls")

    metin_kutusu = driver.find_element(By.CSS_SELECTOR, "#input-example input")

    assert metin_kutusu.is_displayed() is True      # görünüyor
    assert metin_kutusu.is_enabled() is False       # ama PASİF (disabled)
    print("\n[OK] Input görünür ama pasif -> is_displayed=True, is_enabled=False")

    # 'Enable' butonuna basınca aktifleşiyor
    driver.find_element(By.CSS_SELECTOR, "#input-example button").click()
    driver.find_element(By.ID, "message")  # 'It's enabled!' mesajını bekle (implicit wait)

    assert metin_kutusu.is_enabled() is True
    metin_kutusu.send_keys("artık yazabiliyorum")
    print("[OK] Aktifleştikten sonra yazı yazılabildi.")


# ---------------------------------------------------------------------------
# 2) TEXT INPUT — yazı yazma
# ---------------------------------------------------------------------------

@pytest.mark.etkilesim
def test_yazi_yaz_temizle_ve_uzerine_yaz(driver):
    """
    send_keys() yazıyı EKLER, mevcut yazının üzerine yazmaz.
    Var olan bir değeri değiştireceksen önce clear() çağırmalısın.

    Bu, yeni başlayanların en sık düştüğü tuzaklardan biri:
    'anilanil' gibi birbirine yapışmış değerler hep bu yüzden oluşur.
    """
    driver.get(B + "login")
    kullanici = driver.find_element(By.ID, "username")

    kullanici.send_keys("anil")
    assert kullanici.get_attribute("value") == "anil"

    # clear() YAPMADAN tekrar yazarsak ekleniyor:
    kullanici.send_keys("kavak")
    assert kullanici.get_attribute("value") == "anilkavak"
    print(f"\n[!] clear() olmadan: '{kullanici.get_attribute('value')}' (yapıştı)")

    # Doğrusu: önce temizle, sonra yaz
    kullanici.clear()
    kullanici.send_keys("tomsmith")
    assert kullanici.get_attribute("value") == "tomsmith"
    print(f"[OK] clear() sonrası: '{kullanici.get_attribute('value')}'")


@pytest.mark.etkilesim
def test_text_ile_get_attribute_value_farki(driver):
    """
    ÇOK ÖNEMLİ AYRIM (buna herkes takılır):

        .text                    -> etiketin ARASINDAKİ yazı
                                    <h2>Login Page</h2>  ->  "Login Page"
        .get_attribute("value")  -> input kutusunun İÇİNDEKİ değer
                                    <input value="tomsmith">  ->  "tomsmith"

    Bir input'a .text dersen BOŞ string alırsın ve "neden çalışmıyor" diye
    saatlerce uğraşırsın. Input = value, diğer her şey = text.
    """
    driver.get(B + "login")

    baslik = driver.find_element(By.TAG_NAME, "h2")
    assert baslik.text == "Login Page"

    kullanici = driver.find_element(By.ID, "username")
    kullanici.send_keys("tomsmith")

    assert kullanici.text == ""                              # input'ta .text BOŞ!
    assert kullanici.get_attribute("value") == "tomsmith"    # doğrusu bu
    print("\n[OK] Etiket için .text, input için get_attribute('value').")


@pytest.mark.etkilesim
def test_klavye_tuslari_ile_gonderme(driver):
    """
    send_keys() sadece harf değil, KLAVYE TUŞU da gönderebilir (Keys sınıfı).
    Enter'a basmak, forma tıklamadan göndermenin en pratik yolu.
    """
    driver.get(B + "login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    sifre = driver.find_element(By.ID, "password")
    sifre.send_keys("SuperSecretPassword!")
    sifre.send_keys(Keys.RETURN)  # butona tıklamak yerine Enter

    mesaj = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in mesaj
    print("\n[OK] Enter tuşu ile giriş yapıldı (butona tıklamadan).")


# ---------------------------------------------------------------------------
# 3) SELECTING A CHECKBOX — kutucuk işaretleme
# ---------------------------------------------------------------------------

@pytest.mark.etkilesim
def test_checkbox_isaretle_ve_kaldir(driver):
    """
    Checkbox'ta click() bir ANAHTAR değil, bir DEĞİŞTİRİCİDİR (toggle).
    İşaretliyse kaldırır, değilse işaretler.

    Bu sayfada checkbox 1 boş, checkbox 2 zaten işaretli geliyor.
    İkisine de körlemesine click() atarsan biri işaretlenir, diğeri boşalır.
    """
    driver.get(B + "checkboxes")
    kutular = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    assert kutular[0].is_selected() is False   # 1. kutu boş geliyor
    assert kutular[1].is_selected() is True    # 2. kutu işaretli geliyor
    print("\n  Başlangıç: kutu1=boş, kutu2=işaretli")

    kutular[0].click()
    kutular[1].click()

    assert kutular[0].is_selected() is True    # işaretlendi
    assert kutular[1].is_selected() is False   # işareti KALKTI
    print("[!] Körlemesine tıklama ikisini de TERS çevirdi.")


@pytest.mark.etkilesim
def test_checkbox_guvenli_isaretleme_yontemi(driver):
    """
    DOĞRU YÖNTEM: "tıkla" deme, "şu duruma getir" de.
    Önce is_selected() ile sor, sadece gerekiyorsa tıkla.

    Gerçek projede bu küçük fonksiyon sayısız hatayı önler.
    """
    driver.get(B + "checkboxes")
    kutular = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    def duruma_getir(kutu, isaretli_olsun: bool):
        """Kutuyu istenen duruma getirir; zaten o durumdaysa dokunmaz."""
        if kutu.is_selected() != isaretli_olsun:
            kutu.click()

    # İkisini de İŞARETLİ yapmak istiyorum — başlangıç durumları farklı olsa bile
    duruma_getir(kutular[0], True)
    duruma_getir(kutular[1], True)

    assert kutular[0].is_selected() is True
    assert kutular[1].is_selected() is True
    print("\n[OK] İkisi de işaretli — başlangıç durumları farklı olmasına rağmen.")

    # Şimdi ikisini de boşalt
    duruma_getir(kutular[0], False)
    duruma_getir(kutular[1], False)

    assert not kutular[0].is_selected()
    assert not kutular[1].is_selected()
    print("[OK] İkisi de temizlendi.")


# ---------------------------------------------------------------------------
# 4) USING A COMBOBOX — açılır liste (dropdown)
# ---------------------------------------------------------------------------

@pytest.mark.etkilesim
def test_dropdown_select_sinifi_ile_secim(driver):
    """
    <select> elementleri için Selenium'un ÖZEL bir yardımcısı var: Select sınıfı.
    Elle tıklamaya çalışma; Select üç kolay yol sunuyor:

        select_by_visible_text("Option 1")  -> kullanıcının GÖRDÜĞÜ yazıya göre
        select_by_value("1")                -> HTML'deki value attribute'una göre
        select_by_index(1)                  -> sıraya göre (0'dan başlar)

    Hangisi? Mümkünse visible_text — sayfa değişince en az kırılan odur ve
    testi okuyan kişi ne seçildiğini anlar.
    """
    driver.get(B + "dropdown")

    liste = Select(driver.find_element(By.ID, "dropdown"))

    # Listede neler var?
    secenekler = [o.text for o in liste.options]
    print(f"\n  Listedeki seçenekler: {secenekler}")
    assert "Option 1" in secenekler and "Option 2" in secenekler

    # 1. yol: görünen metne göre
    liste.select_by_visible_text("Option 2")
    assert liste.first_selected_option.text == "Option 2"

    # 2. yol: value attribute'una göre
    liste.select_by_value("1")
    assert liste.first_selected_option.text == "Option 1"

    # 3. yol: sıraya göre (0 = 'Please select an option')
    liste.select_by_index(2)
    assert liste.first_selected_option.text == "Option 2"

    print("[OK] Üç seçim yöntemi de çalıştı.")


@pytest.mark.etkilesim
def test_dropdown_baslangic_durumu_ve_secilemeyen_secenek(driver):
    """
    Bu listenin ilk seçeneği ('Please select an option') 'disabled' —
    yani sadece bilgilendirme amaçlı, seçilemez.

    Gerçek formlarda bu çok yaygındır; testte 'seçili değer' kontrolü
    yaparken bunu bilmek gerekir.
    """
    driver.get(B + "dropdown")
    liste = Select(driver.find_element(By.ID, "dropdown"))

    # Sayfa açılışında seçili olan: placeholder metni
    assert liste.first_selected_option.text == "Please select an option"

    ilk_secenek = liste.options[0]
    assert ilk_secenek.get_attribute("disabled") == "true"
    assert ilk_secenek.is_enabled() is False
    print("\n[OK] Placeholder seçeneği pasif (disabled) — seçilemez.")


# ---------------------------------------------------------------------------
# 📌 DERS NOTU — Etkileşim komutları özeti
#
#   .click()                  tıkla (checkbox'ta toggle yapar, dikkat!)
#   .send_keys("yazı")        yaz (EKLER — üzerine yazmaz)
#   .send_keys(Keys.RETURN)   klavye tuşu gönder
#   .clear()                  input'u temizle
#   .submit()                 formu gönder (form içindeki bir elementten)
#   .text                     etiket arasındaki yazı
#   .get_attribute("value")   input'un içindeki değer
#   .is_displayed()           görünüyor mu
#   .is_enabled()             aktif mi
#   .is_selected()            işaretli mi (checkbox/radio)
#   Select(el)                <select> listeleri için özel yardımcı
# ---------------------------------------------------------------------------
