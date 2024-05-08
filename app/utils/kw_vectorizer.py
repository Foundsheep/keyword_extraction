import re
from kiwipiepy import Kiwi
from sklearn.feature_extraction.text import CountVectorizer

kiwi = Kiwi()

def get_vectorizer():

    # 1. '법' 검출 제외
    # 2. '이태원참사 특별법' 같은 띄어쓰기 포함 법 검출
    # 3. 중복으로 발견 시 CountVectorizer를 통한 나타나는 횟수 중요도 파악을 위해 중복 허용
    def __get_law_related_words(text):
        text = text.strip()
        words = re.findall(r"[0-9가-힣]+법\b|'[0-9가-힣 ]+법'\b", text)
        words = [word.replace("'", "") if "'" in word else word for word in words] # quote removed
        # words = list(set(words)) # remove duplicates just in case
        return words
    
    def _tokenize_kr(text):
        tokens = kiwi.tokenize(text)
        words = [t.form for t in tokens if t.tag.startswith("N") or t.tag in ["VV, VA"]]
        law_related_words = __get_law_related_words(text)

        # duplicates in the first place to be removed
        words = [word for word in words if word not in law_related_words]

        # combine them
        words += law_related_words
        return words

    vectorizer = CountVectorizer(tokenizer=_tokenize_kr)
    return vectorizer

