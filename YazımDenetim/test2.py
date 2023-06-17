import turkish_yaz
def main():

    turkish_yaz_denet = turkish_yaz.turkish_yaz()

    text = "..."
    print("Input:",text)

    text = turkish_yaz_denet.kisaltmakontrol(text)

    text = turkish_yaz_denet.NgramYazimKontrolu(text)

    text = turkish_yaz_denet.kelimekontrol(text)

    text = turkish_yaz_denet.kucukHarfeDonustur(text)

    text = turkish_yaz_denet.noktalamaTemizleyicisi(text)

    text = turkish_yaz_denet.noktalama_ekle(text)

    text = turkish_yaz_denet.buyukharf(text)
    print("Output:", text)

if __name__ == "__main__":
    main()
