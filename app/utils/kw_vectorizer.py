import re
from kiwipiepy import Kiwi
from sklearn.feature_extraction.text import CountVectorizer

kiwi = Kiwi()

def get_vectorizer_1():    
    def _tokenize_kr(text):
        tokens = kiwi.tokenize(text)
        words = [t.form for t in tokens if t.tag.startswith("N") or t.tag in ["VV, VA"]]
        law_related_words = get_law_words_by_regex(text)

        # duplicates in the first place to be removed
        words = [word for word in words if word not in law_related_words]

        # combine them
        words += law_related_words
        return words

    vectorizer = CountVectorizer(tokenizer=_tokenize_kr)
    return vectorizer


def get_vectorizer():
    def _tokenize_kr(text):
        tokens = kiwi.tokenize(text)
        words = [t.form for t in tokens if t.tag.startswith("N") or t.tag in ["VV, VA"]]
        return words

    vectorizer = CountVectorizer(tokenizer=_tokenize_kr)
    return vectorizer
