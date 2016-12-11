import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from nltk.stem import WordNetLemmatizer

def wordfreq():

    # read in the text data
    File = open("improveacademic.txt")
    lines = File.read()


#This does word frequency of all parts of speech.

    # #tokenize all; each word is a token
    # tokenizer = RegexpTokenizer(r'\w+')
    # tokens = tokenizer.tokenize(lines.lower())# need to lowercase for lemmatizer
    #
    #
    # # lemmatize the tokens to combine similar words
    # lem = []
    # for token in tokens:
    #     lem.append((nltk.stem.WordNetLemmatizer().lemmatize(token)))
    #
    # # count the words in lem
    # counts = Counter(lem)
    # for value, count in counts.most_common():
    #     print(value, count)


#Only word frequency of nouns. Used this for actual survey analysis

    #tokenize the txt file by sentence
    sentences = nltk.sent_tokenize(lines)

    #get nouns
    nouns = []
    for sentence in sentences:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if 'NN' in pos: #(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')
                nouns.append(word)

    #lemmatize nouns
    lem_nouns = [nltk.stem.WordNetLemmatizer().lemmatize(noun.lower()) for noun in nouns]

    #count lem_nouns
    counts = Counter(lem_nouns)
    for value, count in counts.most_common():
        print(value, count)

wordfreq()
