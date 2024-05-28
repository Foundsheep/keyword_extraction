from ..utils.util_keywords_extraction import tokenize_kr
from ..utils.util_words_recommendation import get_similar_words_from_wwn_api

def run(text):
    words = tokenize_kr(text)
    return_list = []
    
    for word in words:
        keywords = get_similar_words_from_wwn_api(word)
        return_list.extend(keywords)
        
    return return_list

