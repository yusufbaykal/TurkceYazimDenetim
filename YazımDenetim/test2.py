import turkish_yaz

def main():

    turkish_yaz_denet = turkish_yaz.turkish_denet()

    text = ("""
        Bu bir örnek metindir. Metin üzerinde çeşitli işlemler yâpâcağız.
        Örneğin, en çok kullanılan kelimeleri bulacağız.
        Ayrıca, metindeki alfa-numerik olmayan karakterlerin yüzdesini hesaplayacağız.
        Türkçe karakterlerin düzgün bir şekilde temizlendiğini kontrol edeceğiz.
        Metindeki harf dönüşümlerini yapacağız.
        Metindeki noktalama işaretlerini temizleyeceğiz.
        Stop kelimeleri kaldıracağız.
        HTML etiketlerini kaldıracağız.
    """)
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
