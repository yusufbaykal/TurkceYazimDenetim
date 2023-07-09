import re
import nltk
import turkish_nlp_preprocessing


def main():
    turkish_nlp = turkish_nlp_preprocessing.TurkishNLP()

    metin = """
    <html>
    <head>
        <title>Örnek Metin</title>
    </head>
    <body>
        Bu bir örnek metindir. Metin üzerinde çeşitli işlemler yâpâcağız.
        Örneğin, en çok kullanılan kelimeleri bulacağız.
        Ayrıca, metindeki alfa-numerik olmayan karakterlerin yüzdesini hesaplayacağız.
        Türkçe karakterlerin düzgün bir şekilde temizlendiğini kontrol edeceğiz.
        Metindeki harf dönüşümlerini yapacağız.
        Metindeki noktalama işaretlerini temizleyeceğiz.
        Stop kelimeleri kaldıracağız.
        HTML etiketlerini kaldıracağız.
    </body>
    </html>
    """
    print("HTML etiketleri temizleniyor...")
    temiz_metin = turkish_nlp.htmlEtiketleriniKaldir(metin)
    print(temiz_metin)


    print("\nEn çok kullanılan kelimeler:")
    turkish_nlp.enCokKelime(temiz_metin)


    print("\nAlfa-numeric olmayan karakterlerin yüzdesi hesaplanıyor...")
    alfa_numerik_yuzdesi = turkish_nlp.alfaNumerik(temiz_metin)
    print("Alfa-numeric olmayan karakterlerin yüzdesi: {:%}".format(alfa_numerik_yuzdesi))

    print("\nHarf dönüşümleri yapılıyor...")
    temiz_metin = turkish_nlp.harfDonusum(temiz_metin)
    print(temiz_metin)

    print("\nTürkçe karakterler temizleniyor...")
    temiz_metin = turkish_nlp.turkceKarakter(temiz_metin)
    print(temiz_metin)


    print("\nNoktalama işaretleri temizleniyor...")
    temiz_metin = turkish_nlp.noktalamaTemizleyicisi(temiz_metin)
    print(temiz_metin)


    print("\nStop kelimeleri kaldırılıyor...")
    temiz_metin = turkish_nlp.stopKelimeleriKaldir(temiz_metin)
    print(temiz_metin)


    print("\nKelime sayısı hesaplanıyor...")
    kelime_istatistikleri = turkish_nlp.kelimeSayici(temiz_metin)
    print("Kelime sayısı: {}".format(kelime_istatistikleri['kelimeSayisi']))
    print("Karakter sayısı: {}".format(kelime_istatistikleri['karakterSayisi']))
    print("Benzersiz kelime sayısı: {}".format(kelime_istatistikleri['benzersizKelimeSayisi']))
    print("Benzersiz kelimeler: {}".format(kelime_istatistikleri['benzersizKelimeler']))

if __name__ == "__main__":
    main()
