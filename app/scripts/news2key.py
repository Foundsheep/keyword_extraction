from ..utils.parser import get_text_from_url
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

        concatenated_keywords = ",".join(keywords)
        keywords_list.append(concatenated_keywords)
    return keywords_list
