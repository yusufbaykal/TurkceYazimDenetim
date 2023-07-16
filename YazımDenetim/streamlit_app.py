import streamlit as st
from streamlit_tags import st_tags
import turkish_yaz
import turkish_nlp_preprocessing
turkish_yaz_func = turkish_yaz.turkish_denet
turkish_nlp = turkish_nlp_preprocessing.TurkishNLP


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
                text = turkish_yaz_func.kisaltmakontrol(text)
            elif selected_menu == "Kelime Kontrol":
                text = turkish_yaz_func.kelimekontrol(text)
            elif selected_menu == "Noktalama İşareti Ekle":
                text = turkish_yaz_func.noktalama_ekle(text)
            elif selected_menu == "Yazım Denetimi":
                text = turkish_yaz_func.NgramYazimKontrolu(text)
            elif selected_menu == "HTML Etiketleri Temizleme":
                text = turkish_nlp.htmlEtiketleriniKaldir(text)
            elif selected_menu == "En Çok Kullanılan Kelimeler":
                text = turkish_nlp.enCokKelime(text)
            elif selected_menu == "Alfa-Numeric":
                text = turkish_nlp.alfaNumerik(text)
            elif selected_menu == "Harf Dönüşümü":
                text = turkish_nlp.harfDonusum(text)
            elif selected_menu == "Türkçe Karakter Olmayan":
                text = turkish_nlp.turkceKarakter(text)
            elif selected_menu == "Noktalama İşareti Kaldır":
                text = turkish_nlp.noktalamaTemizleyicisi(text)
            elif selected_menu == "Stop-Words Kaldır":
                text = turkish_nlp.stopKelimeleriKaldir(text)
            elif selected_menu == "Kelime İstatistikleri":
                text = turkish_nlp.kelimeSayici(text)
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
            text = turkish_yaz_func.kisaltmakontrol(text)
            text = turkish_yaz_func.NgramYazimKontrolu(text)
            text = turkish_yaz_func.kelimekontrol(text)
            text = turkish_yaz_func.kucukHarfeDonustur(text)
            text = turkish_yaz_func.noktalamaTemizleyicisi(text)
            text = turkish_yaz_func.noktalama_ekle(text)
            text = turkish_yaz_func.buyukharf(text)

            st.write("Denetleme Sonucu")
            st.write(text)
        else:
            st.warning("Metin Girişi Gerçekleştirmediniz.")


if __name__ == '__main__':
    main()
