import streamlit as st
import turkish_yaz
import  turkish_nlp_preprocessing
turkish_yaz_denet = turkish_yaz.turkish_yaz()
turkish_nlp = turkish_nlp_preprocessing.TurkishNLP()


def main():
    st.title("Türkçe Yazım Denetimi")

    page = st.sidebar.selectbox("Sayfa Seçiniz", ("Yazım Denetimi", "Analizler & Veri Ön İşleme"))

    if page == "Yazım Denetimi":
        yazim_denetimi()
    elif page == "Analizler & Veri Ön İşleme":
        turkish_data_preprocessing()

def turkish_data_preprocessing():

    menu = ["Kısaltma Kontrol", "Kelime Kontrol", "Noktalama İşareti Ekle", "Yazım Denetimi",
            "HTML Etiketleri Temizleme","En Çok Kullanılan Kelimeler","Alfa-Numeric",
            "Harf Dönüşümü","Türkçe Karakter Olmayan","Noktalama İşareti Kaldır",
            "Stop-Words Kaldır","Metin İstatistikleri"]

    selected_menu = st.sidebar.selectbox("İşlem Seçiniz", menu)

    metin = st.text_area("Metin Girin")

    if st.button("Denetle"):
        if metin:
            if selected_menu == "Kısaltma Kontrol":
                text = turkish_yaz_denet.kisaltmakontrol(metin)
            elif selected_menu == "Kelime Kontrol":
                text = turkish_yaz_denet.kelimekontrol(metin)
            elif selected_menu == "Noktalama İşareti Ekle":
                text = turkish_yaz_denet.noktalama_ekle(metin)
            elif selected_menu == "Yazım Denetimi":
                text = turkish_yaz_denet.NgramYazimKontrolu(metin)
            elif selected_menu == "HTML Etiketleri Temizleme":
                text = turkish_nlp.htmlEtiketleriniKaldir(metin)
            elif selected_menu == "En Çok Kullanılan Kelimeler":
                text = turkish_nlp.enCokKelime(metin)
            elif selected_menu == "Alfa-Numeric":
                text = turkish_nlp.alfaNumerik(metin)
            elif selected_menu == "Harf Dönüşümü":
                text = turkish_nlp.harfDonusum(metin)
            elif selected_menu == "Türkçe Karakter Olmayan":
                text = turkish_nlp.turkceKarakter(metin)
            elif selected_menu == "Noktalama İşareti Kaldır":
                text = turkish_nlp.noktalamaTemizleyicisi(metin)
            elif selected_menu == "Stop-Words Kaldır":
                text = turkish_nlp.stopKelimeleriKaldir(metin)
            elif selected_menu == "Kelime İstatistikleri":
                text = turkish_nlp.kelimeSayici(metin)
                kelimeSayisi = text['kelimeSayisi']
                karakterSayisi = text['karakterSayisi']
                benzersizKelimeSayisi = text['benzersizKelimeSayisi']
                benzersizKelimeler = text['benzersizKelimeler']

            st.write("Denetleme Sonucu")
            st.write(text)

        else:
            st.warning("Metin Girişi Gerçekleştirmediniz.")

    return


def yazim_denetimi():
    st.subheader("Yazım Denetimi")
    metin = st.text_area("Metin Girin")

    if st.button("Denetle"):
        if metin:
            text = turkish_yaz_denet.kisaltmakontrol(metin)
            text = turkish_yaz_denet.NgramYazimKontrolu(text)
            text = turkish_yaz_denet.kelimekontrol(text)
            text = turkish_yaz_denet.kucukHarfeDonustur(text)
            text = turkish_yaz_denet.noktalamaTemizleyicisi(text)
            text = turkish_yaz_denet.noktalama_ekle(text)
            text = turkish_yaz_denet.buyukharf(text)

            st.write("Denetleme Sonucu")
            st.write(text)
        else:
            st.warning("Metin Girişi Gerçekleştirmediniz.")


if __name__ == '__main__':
    main()
