import sys
sys.path.append("/path/to/SpellChecker")

import re
import locale
import Corpus
from YazımDenetim import listeler
from ngram import NGram
from Dictionary.Word import Word
from Corpus.Sentence import Sentence
from NGram.NoSmoothing import NoSmoothing
from SpellChecker.NGramSpellChecker import NGramSpellChecker
from SpellChecker.SimpleSpellChecker import SimpleSpellChecker
from SpellChecker.TrieBasedSpellChecker import TrieBasedSpellChecker
from SpellChecker.SpellCheckerParameter import SpellCheckerParameter
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer


class turkish_denet():
    nGram = NGram('./data/ngram.txt')
    def __init__(self, text=""):
        self.fsm = FsmMorphologicalAnalyzer()
        self.parameter = SpellCheckerParameter()
        self.nGram = NGram("./data/ngram.txt")
        self.text = text
        self.searchfile = open("./data/VERB_TS_Corpus_Frequency_List.txt", "r", encoding="utf8")
        self.trieSpellChecker = TrieBasedSpellChecker(self.fsm, self.nGram, self.parameter)
        self.nGramSpellChecker = NGramSpellChecker(self.fsm, self.nGram, self.parameter)
        self.turkcekelime = []



    def kisaltmakontrol(self,text):
        kisaltList = listeler.kisaltList
        uzunhaller = listeler.uzunhaller
        words = text.split()
        for i in range(len(words)):
            if words[i] in kisaltList:
                index = kisaltList.index(words[i])
                words[i] = uzunhaller[index]
        result = " ".join(words)
        result = " ".join(result.split())
        return text

    def kelimekontrol(self, text):
        kelimeler = set(self.turkcekelime)
        generated_words = set()
        misspellings = {}
        context_list = []
        turkish_word = set()


        with open("./data/generated_words.txt", "r", encoding="utf-8") as file:
            for line in file:
                generated_words.add(line.strip())


        with open("./data/turkish_dictionary.txt", "r", encoding="utf-8") as file:
            for line in file:
                self.turkcekelime.append(line.strip())


        with open("./data/turkish_misspellings.txt", "r", encoding="utf-8") as file:
            for line in file:
                correct_word, misspelled_word = line.strip().split()
                misspellings[misspelled_word] = correct_word


        with open("./data/turkish_words.txt","r",encoding="utf-8") as file:
            for line in file:
                turkish_word.add(line.strip())



        with open("./data/context_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                context_list.append(line.strip())

        words = text.split()
        filtered_words = []
        for word in words:
            ana_kelime = word.strip(",.!?")
            if ana_kelime in kelimeler:
                filtered_words.append(word)
            elif ana_kelime in generated_words:
                filtered_words.append(word)
            elif ana_kelime in misspellings:
                filtered_words.append(word)
            elif ana_kelime in turkish_word:
                filtered_words.append(word)
            else:
                filtered_words.append("")

        filtered_text = " ".join(filtered_words)


        for context in context_list:
            if context in filtered_text:
                filtered_text = filtered_text.replace(context, "")


        with open("./data/filtered_text.txt", "w", encoding="utf-8") as file:
            file.write(filtered_text)

        return filtered_text

    def kucukHarfeDonustur(self,text):
        words = text.split()
        lowercased_words = [word.lower() for word in words]
        return " ".join(lowercased_words)

    def noktalamaTemizleyicisi(self, text):
        regex = r"(?<!\d)[.,;:?)(](?!\d)"
        result = re.sub (regex, "", text, 0)
        return result

    def TrieYazimKontrolu(self, text):
        return self.trieSpellChecker.spellCheck (Sentence (text)).toString ()

    def NgramYazimKontrolu(self, text):
        self.nGramSpellChecker.spellCheck(Sentence(text))
        return text
    """def noktalama_ekle(self,text):
        kelimeler = text.split()
        baglaclar = listeler.baglaclar
        yeni_metin = ""

        for i, kelime in enumerate(kelimeler):
            son_harf = kelime[-1]
            son_kelime = kelimeler[-1]

            if son_harf.isalpha() or son_harf.isdigit():
                if kelime.endswith(("ar", "er", "ır", "ir", "ur", "ür")):
                    yeni_metin += kelime + ","
                elif kelime.endswith(("de", "den", "da", "den")):
                    yeni_metin += kelime + ","
                else:
                    yeni_metin += kelime + " "

                    if kelime.endswith(("ruz", "tı", "di", "yor")):
                        if son_kelime != ".":
                            yeni_metin = yeni_metin.rstrip() + "."
            elif kelime.lower() in baglaclar:
                if i < len(kelimeler) - 1:
                    yeni_metin += kelime + ","
                else:
                    yeni_metin += kelime + "."
            else:
                yeni_metin += kelime + " "

        return yeni_metin.strip()"""

    def noktalama_ekle(self, text):
        with open('./data/turkish_dictionary.txt', 'r', encoding='utf-8') as file:
            dictionary = {}
            for line in file:
                word, tags = line.strip().split(' ', 1)
                dictionary[word] = tags

        kelimeler = text.split()
        yeni_metin = ""

        for i, kelime in enumerate(kelimeler):
            if kelime in dictionary:
                tags = dictionary[kelime]
                if "IS_ADJ" in tags or "IS_ADJ+" in tags:
                    yeni_metin += kelime + ", "
                elif "IS_SD" in tags or "IS_SD+" in tags:
                    yeni_metin += kelime + ". "
                else:
                    yeni_metin += kelime + " "
            else:
                yeni_metin += kelime + " "

            if i < len(kelimeler) - 1 and kelime.endswith((".", ",", "?", "!")):
                yeni_metin += " "

        yeni_metin = yeni_metin.rstrip(",") + "."
        return yeni_metin.strip()

    def buyukharf(self, text):
        kelimeler = text.split()
        capitalized_words = []

        for i, word in enumerate(kelimeler):
            if len(word) > 0:
                if i == 0:
                    capitalized_word = word[0].upper() + word[1:].lower()
                elif kelimeler[i - 1].endswith((".", "?", "!")):
                    capitalized_word = word[0].upper() + word[1:].lower()
                else:
                    capitalized_word = word.lower()
                capitalized_words.append(capitalized_word)

        buyukharf = ' '.join(capitalized_words)
        return buyukharf








