from kiwipiepy import Kiwi
from sklearn.feature_extraction.text import CountVectorizer

kiwi = Kiwi()

def get_vectorizer():
    def _tokenize_kr(text):
        tokens = kiwi.tokenize(text)
        words = [t.form for t in tokens if t.tag.startswith("N") or t.tag in ["VV, VA"]]
        return words

    vectorizer = CountVectorizer(tokenizer=_tokenize_kr)
    return vectorizer