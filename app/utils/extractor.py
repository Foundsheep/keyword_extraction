from ..models import kw_model
from . import vectorizer
from .parser import get_law_words_by_regex, get_law_words_by_json

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

    