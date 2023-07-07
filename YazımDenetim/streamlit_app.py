import streamlit as st
import turkish_yaz

turkish_yaz_denet = turkish_yaz.turkish_yaz()


def main():
    st.title("Türkçe Yazım Denetimi")

    page = st.sidebar.selectbox("Sayfa Seçiniz", ("Yazım Denetimi", "Analizler & Veri Ön İşleme"))

    if page == "Yazım Denetimi":
        yazim_denetimi()
    elif page == "Analizler & Veri Ön İşleme":
        turkish_data_preprocessing()


def corpus_turkish():
    pass

def turkish_data_preprocessing():
    st.title("Türkçe Yazım Denetimi")

    menu = ["Kısaltma Kontrol", "Kelime Kontrol", "Noktalama İşareti Ekle", "Yazım Denetimi"]

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
