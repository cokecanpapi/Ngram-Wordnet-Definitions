# Ngram-Wordnet-Definitions

This repository contains a Python script that demonstrates how to extract definitions from WordNet for n-grams (sequences of n words) found in a given text. It uses the NLTK library to tokenize the text, extract n-grams, and retrieve definitions from WordNet for each n-gram.

## How to Use
1. Install the required dependencies by running:
   ```sh
   pip install nltk
   ```
2. Run the script `main.py`:
   ```sh
   python ngram_definitions.py
   ```
3. Enter a sentence when prompted.

The script will then print the n-grams found in the sentence along with their definitions from WordNet, if available.

## Dependencies
- nltk

## Citations
- NLTK documentation: [NLTK 3.6.2 documentation](https://www.nltk.org/index.html)
- WordNet: Fellbaum, Christiane (1998, ed.) WordNet: An Electronic Lexical Database. Cambridge, MA: MIT Press. [WordNet](https://direct.mit.edu/books/book/1928/WordNetAn-Electronic-Lexical-Database)
- Python’s official documentation for the `str.translate` and `str.maketrans` functions: [Python 3.9.7 Documentation](https://docs.python.org/3/library/stdtypes.html)
- Python’s official documentation for the `ngrams` function: [nltk.util.ngrams](https://www.nltk.org/_modules/nltk/util.html)
