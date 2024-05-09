from ..utils.parser import get_text_from_url, get_law_words_by_json, get_law_words_by_regex
from ..models import kw_model
from ..utils import vectorizer

def run(url_list, threshold=0.0, top_n=10):
    keywords_list = []
    for url in url_list:
        print(f"{url = }")
        text = get_text_from_url(url)
        keywords_tuple = kw_model.extract_keywords(text, vectorizer=vectorizer, top_n=top_n)
        
        keywords = []
        for tup in keywords_tuple:
            if tup[1] >= threshold:
                keywords.append(tup[0])
                print(f"[{tup[0]}] keyword, probability :[{tup[1]}]")
            else:
                print(f"[{tup[0]}] keyword has been excluded with threshold :[{tup[1]}]")

        # law names by regex
        regex_law_names = get_law_words_by_regex(text)

        # law names by json
        json_law_names = get_law_words_by_json(text)

        # combine them all
        # TODO: change the logic 1. to achieve top_n 
        # TODO: 2. check if law names in keywords before 1
        keywords = keywords + regex_law_names + json_law_names
        keywords = list(set(keywords))

        concatenated_keywords = ",".join(keywords)
        keywords_list.append(concatenated_keywords)

    return keywords_list
