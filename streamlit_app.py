import streamlit as st
from YazımDenetim.turkish_yaz import turkish_denet
from YazımDenetim.turkish_nlp_preprocessing import TurkishNLP
denetci = turkish_denet()
turknlp = TurkishNLP()
st.set_page_config(
    layout="centered", page_title="Türkçe Yazım Denetim", page_icon="❄️"
)

def main():

    c1, c2 = st.columns([0.30, 2])
    with c1:
        st.image(
                "../Images/logo.png",
                width=95,
            )
    with c2:
        st.caption("")
        st.title("Türkçe Yazım Denetimi")

    page = st.sidebar.selectbox("Sayfa Seçiniz", ("Yazım Denetimi", "Analizler & Veri Ön İşleme"))

    if page == "Yazım Denetimi":
        yazim_denetimi()
    elif page == "Analizler & Veri Ön İşleme":
        turkish_data_preprocessing()

    st.sidebar.write(
        """

    App created by [Yusuf Baykaloğlu](https://www.linkedin.com/in/yusufbaykaloglu/) using [Githup](https://github.com/yusufbaykal) and [HuggingFace](https://huggingface.co/yusufbaykaloglu) and
    [Medium](https://medium.com/@yusufbaykaloglu)
    """
    )


def turkish_data_preprocessing():
    st.subheader("Data Preprocessing")
    st.markdown(
        """
        <style>
        .css-1l02zno {
            position: absolute;
            top: 0;
            right: 0;
        }
        </style>
        <a href="https://github.com/yusufbaykal/TurkceYazimDenetim" target="_blank" class="css-1l02zno">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="30" height="30">
        </a>
        """,
        unsafe_allow_html=True,
    )

    menu = ["Kısaltma Kontrol", "Kelime Kontrol", "Noktalama İşareti Ekle", "Yazım Denetimi",
            "HTML Etiketleri Temizleme","En Çok Kullanılan Kelimeler","Alfa-Numeric",
            "Harf Dönüşümü","Türkçe Karakter Olmayan","Noktalama İşareti Kaldır",
            "Stop-Words Kaldır","Metin İstatistikleri"]

    selected_menu = st.sidebar.selectbox("İşlem Seçiniz", menu)

    text = st.text_area("Metin Girin")
    if st.button("Denetle"):
        if text:
            if selected_menu == "Kısaltma Kontrol":
                text = denetci.kisaltmakontrol()
            elif selected_menu == "Kelime Kontrol":
                text = denetci.kelimekontrol()
            elif selected_menu == "Noktalama İşareti Ekle":
                text = denetci.noktalama_ekle()
            elif selected_menu == "Yazım Denetimi":
                text = denetci.NgramYazimKontrolu()
            elif selected_menu == "HTML Etiketleri Temizleme":
                text = denetci.htmlEtiketleriniKaldir()
            elif selected_menu == "En Çok Kullanılan Kelimeler":
                text = denetci.enCokKelime()
            elif selected_menu == "Alfa-Numeric":
                text = denetci.alfaNumerik()
            elif selected_menu == "Harf Dönüşümü":
                text = turknlp.harfDonusum()
            elif selected_menu == "Türkçe Karakter Olmayan":
                text = turknlp.turkceKarakter()
            elif selected_menu == "Noktalama İşareti Kaldır":
                text = turknlp.noktalamaTemizleyicisi()
            elif selected_menu == "Stop-Words Kaldır":
                text = turknlp.stopKelimeleriKaldir()
            elif selected_menu == "Kelime İstatistikleri":
                text = turknlp.kelimeSayici()
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
    st.markdown(
        """
        <style>
        .css-1l02zno {
            position: absolute;
            top: 0;
            right: 0;
        }
        </style>
        <a href="https://github.com/yusufbaykal/TurkceYazimDenetim" target="_blank" class="css-1l02zno">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="30" height="30">
        </a>
        """,
        unsafe_allow_html=True,
    )

    text = st.text_area("Metin Girin")
    if st.button("Denetle"):
        if text:
            text = denetci.NgramYazimKontrolu()
            text = denetci.kisaltmakontrol()
            text = denetci.keliekontrol()
            text = denetci.kucukHarfeDonustur()
            text = denetci.noktalamaTemizleyicisi()
            text = denetci.noktalama_ekle()
            text = denetci.buyukharf()

            st.write("Denetleme Sonucu")
            st.write(text)
        else:
            st.warning("Metin Girişi Gerçekleştirmediniz.")


if __name__ == '__main__':
    main()
