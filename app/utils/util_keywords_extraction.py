
import re
import requests
from time import time
from bs4 import BeautifulSoup
from kiwipiepy import Kiwi
from sklearn.feature_extraction.text import CountVectorizer

from . import data
from ..models import kw_model


def get_text_from_url(url):
    r = requests.get(url=url)

    text = None
    if r.status_code == 200:
        print(f"[{url}] url sent 200 code")        
        soup = BeautifulSoup(r.content, "html5lib")
        dic_area = soup.select_one("#dic_area")
        if dic_area is not None:
            text = dic_area.get_text()
            text = text.strip()
        else:
            print(f"dic_area not found on url = [{url}]")
    else:
        print(f"[{url}] url content not found")
    return text


# 1. '법' 검출 제외
# 2. '이태원참사 특별법' 같은 띄어쓰기 포함 법 검출
def get_law_words_by_regex(text):
    text = text.strip()

    # 1. ~~~법
    # 2. '~~ 법'
    words = re.findall(r"[0-9가-힣]+법\b|'[0-9가-힣 ]+법'", text)

    # 1, 2 -> 법령
    words += re.findall(r"[0-9가-힣]+법령\b|'[0-9가-힣 ]+법령'", text)

    # 후처리
    words = [word.replace("'", "") if "'" in word else word for word in words] # quote removed
    
    # remove duplicates
    words = list(set(words))
    print(f"regex found {words}")
    return words


def get_law_words_by_json(text):
    result_list = []
    law_names = list(data.values())
    
    print("law name matching based on json begins")
    
    # search begins
    start = time()
    for name in law_names:
        if name in text:
            result_list.append(name)
            print(f"[{name}] found")
    end = time()
    
    # print timing
    duration = end - start
    prefix = "search spent "
    if duration >= 60:
        report_sentence = prefix + f"[{int(duration // 60)} minutes, {duration % 60 :.2f} seconds]"
    else:
        report_sentence = prefix + f"[{duration :.2f} seconds]"
    print(report_sentence)
    
    # remove duplicates
    result_list = list(set(result_list))
    return result_list


kiwi = Kiwi()
def tokenize_kr(text):
    tokens = kiwi.tokenize(text)
    words = [t.form for t in tokens if t.tag.startswith("N") or t.tag in ["VV, VA"]]
    return words



def get_law_names(text):
    # law names by regex
    regex_law_names = get_law_words_by_regex(text)

    # law names by json
    json_law_names = get_law_words_by_json(text)

    # get a new top_n
    law_names = list(set(regex_law_names + json_law_names))

    return law_names


def calculate_new_top_n(law_names, top_n):
    original_top_n = top_n
    top_n -= len(law_names)
    
    # if new_top_n is not a positive number
    if top_n < 1 :
        print(f"the number of pre-found law_names : [{len(law_names)}] >= original top_n : [{original_top_n}]")
        top_n = 10
        print(f"So top_n is set to [{top_n}] and will output [{top_n + len(law_names)}] keywords, if they all are above threshold")
    
    return top_n

vectorizer = CountVectorizer(tokenizer=tokenize_kr)
def extract_keywords_by_keybert_with_law_names(text, top_n, threshold):
    law_names = get_law_names(text)
    top_n = calculate_new_top_n(law_names, top_n)

    # use keybert
    keywords_tuple = kw_model.extract_keywords(text, vectorizer=vectorizer, top_n=top_n)
    
    keywords = []
    for tup in keywords_tuple:
        if tup[1] >= threshold:
            keywords.append(tup[0])
            print(f"[{tup[0]}] keyword, probability :[{tup[1]}]")
        else:
            print(f"[{tup[0]}] keyword has been excluded with threshold :[{tup[1]}]")

    # combine them all
    keywords = keywords + law_names
    keywords = list(set(keywords))
    
    return keywords