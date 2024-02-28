import nltk
from nltk.corpus import wordnet
from nltk.util import ngrams
import string

nltk.download('punkt')
nltk.download('wordnet')

def get_def(word):
    synsets = wordnet.synsets(word)
    definitions = []
    if synsets:
        for synset in synsets:
            definitions.append(synset.definition())
        return definitions
    else:
        return None

def tokenize(text):
    return nltk.word_tokenize(text)

def ngram_def(text, n):
    tokens = tokenize(text)
    punc = str.maketrans('', '', string.punctuation)
    tokens = [token.translate(punc) for token in tokens]
    ngram_list = list(ngrams(tokens, n))
    for ngram in ngram_list:
        ngram_string = "_".join(ngram)
        definition = get_def(ngram_string.lower())
        if definition is not None:
            definition = "<< or >>".join(definition)
            print(ngram_string,",",definition.replace(';',"<< and >>"))
        else:
            print(ngram_string,",")

text = input("Enter a sentence: ")

for n in range(2, 5):
    print(f"{n} level n-gram \n")
    ngram_defs = ngram_def(text, n)
    print("\n")

######CITATIONS######
# NLTK documentation: NLTK 3.6.2 documentation  https://www.nltk.org/index.html
# WordNet: Fellbaum, Christiane (1998, ed.) WordNet: An Electronic Lexical Database. Cambridge, MA: MIT Press. https://direct.mit.edu/books/book/1928/WordNetAn-Electronic-Lexical-Database
# Python’s official documentation for the str.translate and str.maketrans functions: Python 3.9.7 Documentation  https://docs.python.org/3/library/stdtypes.html
# Python’s official documentation for the ngrams function: nltk.util.ngrams   https://www.nltk.org/_modules/nltk/util.html