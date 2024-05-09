from ..utils.parser import get_text_from_url, get_law_words_by_json, get_law_words_by_regex
from ..models import kw_model
from ..utils import vectorizer

def run(url_list, threshold=0.0, top_n=10):
    keywords_list = []
    for url in url_list:
        print(f"{url = }")

        # TODO: try, except to catch the url provided doesn't match the naver news html structure
        text = get_text_from_url(url)
        # law names by regex
        regex_law_names = get_law_words_by_regex(text)

        # law names by json
        json_law_names = get_law_words_by_json(text)

        # get a new top_n
        law_names = list(set(regex_law_names + json_law_names))
        original_top_n = top_n
        top_n -= len(law_names)
        if top_n < 1 :
            print(f"the number of pre-found law_names : [{len(law_names)}] >= original top_n : [{original_top_n}]")
            top_n = 10
            print(f"So top_n is set to [{top_n}] and will output [{top_n + len(law_names)}] keywords, if they all are above threshold")

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

        concatenated_keywords = ",".join(keywords)
        keywords_list.append(concatenated_keywords)

    return keywords_list
