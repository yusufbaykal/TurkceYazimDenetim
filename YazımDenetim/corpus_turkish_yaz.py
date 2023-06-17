from NGram.NGram import NGram
from Corpus.Corpus import Corpus
from Corpus.Sentence import Sentence
from SpellChecker.NGramSpellChecker import NGramSpellChecker
from SpellChecker.TrieBasedSpellChecker import TrieBasedSpellChecker
from SpellChecker.SpellCheckerParameter import SpellCheckerParameter
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

fsm = FsmMorphologicalAnalyzer()
ngram = NGram("../data/....")
parameter = SpellCheckerParameter()
spellChecker = NGramSpellChecker(fsm, ngram, parameter)
sentence = Sentence("input text")
corrected = spellChecker.spellCheck(sentence)
print(corrected)