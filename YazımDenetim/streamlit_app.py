import streamlit as st
import  turkish_yaz

turkish_yaz_denet = turkish_yaz.turkish_yaz()

def main():
    st.title("Türkçe Yazım Denetimi")

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
            sonuc = text
            st.write("Denetleme Sonucu:")
            st.write(sonuc)
        else:
            st.warning("Metin girişi yapmadınız.")

if __name__ == '__main__':
    main()
