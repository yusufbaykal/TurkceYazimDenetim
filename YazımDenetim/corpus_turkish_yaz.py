import turkish_yaz
from NGram.NGram import NGram
from Corpus.Corpus import Corpus
from Corpus.Sentence import Sentence
from SpellChecker.NGramSpellChecker import NGramSpellChecker
from SpellChecker.TrieBasedSpellChecker import TrieBasedSpellChecker
from SpellChecker.SpellCheckerParameter import SpellCheckerParameter
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

def corpusturkish():
    fsm = FsmMorphologicalAnalyzer()
    ngram = NGram("../data/....")
    parameter = SpellCheckerParameter()
    spellChecker = NGramSpellChecker(fsm, ngram, parameter)
    sentence = Sentence("input text")
    corrected = spellChecker.spellCheck(sentence)
    print(corrected)

    
def corpusfunctionturkish():
    turkish_yaz_denet = turkish_yaz.turkish_denet()
    fsm = FsmMorphologicalAnalyzer()
    ngram = NGram("../data/....")
    parameter = SpellCheckerParameter()
    spellChecker = NGramSpellChecker(fsm, ngram, parameter)
    sentence = Sentence("input text")
    sentence = turkish_yaz_denet.kisaltmakontrol(sentence)
    sentence = turkish_yaz_denet.NgramYazimKontrolu(sentence)
    sentence = turkish_yaz_denet.kelimekontrol(sentence)
    sentence = turkish_yaz_denet.kucukHarfeDonustur(sentence)
    sentence = turkish_yaz_denet.noktalamaTemizleyicisi(sentence)
    sentence = turkish_yaz_denet.noktalama_ekle(sentence)
    sentence = turkish_yaz_denet.buyukharf(sentence)
    print("Output:", sentence)
    corrected = spellChecker.spellCheck(sentence)
    print(corrected)
