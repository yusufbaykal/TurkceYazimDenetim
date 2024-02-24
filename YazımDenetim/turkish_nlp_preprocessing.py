import nltk
import pandas as pd
from bs4 import BeautifulSoup
import string
import re
import timeit
from IPython.display import Image
import spacy
from YazımDenetim import listeler

class TurkishNLP():
    def enCokKelime(self,text):
        kelimeAyir = nltk.FreqDist(text.lower().split())
        for kelime, sayi in kelimeAyir.most_common(20):
            print(kelime, sayi, end=" ")

        return kelimeAyir

    def alfaNumerik(self,text):
        numerikKarakter = sum(len(w) for w in text.split() if not w.isalnum())
        numerikKarakterYuzdesi = numerikKarakter / len(text.replace(" ", ""))

        print("Toplamda Karakter Sayılmayan Değişken Sayısı: {}".format(numerikKarakter))
        print("Toplamda Karakter olmayanların Total Metin içerisindeki Yüzdesi: {:%}".format(numerikKarakterYuzdesi))

        return numerikKarakterYuzdesi

    def turkceKarakter(self,text):
        alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz0123456789 ' + '\n'
        cleanedText = ''
        for char in text:
            if char in alfabe:
                cleanedText = cleanedText + char

        return cleanedText

    def harfDonusum(self,text):
        text = re.sub(r"Â", "A", text)
        text = re.sub(r"â", "a", text)
        text = re.sub(r"Î", "I", text)
        text = re.sub(r"î", "ı", text)
        text = re.sub(r"Û", "U", text)
        text = re.sub(r"û", "u", text)

        return text

    def kelimeSayici(self,text):

        kelimeler = text.split(" ")
        kelimeSayisi = len(kelimeler)
        karakterSayisi = len(text)
        benzersizKelimeSayisi = len(set(kelimeler))
        benzersizKelimeler = sorted(list(set(kelimeler)))

        return {
            'kelimeSayisi': kelimeSayisi,
            'karakterSayisi': karakterSayisi,
            'benzersizKelimeSayisi': benzersizKelimeSayisi,
            'benzersizKelimeler': benzersizKelimeler
        }
        def kucukHarfeDonustur(text):
            return text.lower()

        def noktalamaIsaretleriniKaldir(self,text):
            return re.sub(r'[^\w\s]', '', text)

        text = re.sub(r"\n", " ", text)
        text = re.sub(r"  ", " ", text)

        text = re.sub(r"I", "ı", text)
        text = kucukHarfeDonustur(text)
        text = noktalamaIsaretleriniKaldir(text)


    def noktalamaTemizleyicisi(self,text):
        regex = r"(?<!\d)[.,;:?)(](?!\d)"
        result = re.sub(regex, "", text, 0)
        return result

    def stopKelimeleriKaldir(self,text):
        with open('../data/stopwords.txt', 'r', encoding='utf-8') as f:
            stopKelimeler = set(f.read().splitlines())

        return ' '.join([kelime for kelime in text.split() if kelime.lower() not in stopKelimeler])

    def htmlEtiketleriniKaldir(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text(" ")
        return text

    def kisaltmakontrol(self, text):
        kisaltList = listeler.kisaltList
        uzunhaller = listeler.uzunhaller
        words = text.split()
        for i in range(len(words)):
            if words[i] in kisaltList:
                index = kisaltList.index(words[i])
                words[i] = uzunhaller[index]
        result = " ".join(words)
        result = " ".join(result.split())
        return result

