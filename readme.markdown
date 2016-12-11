UCA Survey
================

Tool that uses NLTK (Natural Language Tool Kit) to analyze short answer survey responses and return keywords based on frequency.

Reads in text responses from a survey. Then, using NLTK, it tokenizes sentences. Can choose to keep all words or only nouns. Then lemmatizes in order to group similar words. It then counts the lemmatized tokens and returns the words in order of most commonly used.

To run: install NLTK via pip, also will need to install various models including Punkt Tokenizer Model, Averaged Perceptron Tagger, and WordNet Corpora to use WordNetLemmatizer. Can install all these easily-- 1) in terminal run Python, 2) type "import nltk" and enter, 3) type "nltk.download()" and enter, 4) use the tool that comes up to download what you need. Look around in the different model, packages, corpora tabs.
