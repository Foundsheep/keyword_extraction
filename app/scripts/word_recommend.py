from ..utils.api_caller import get_similar_words_from_wwn_api
from ..utils.kw_vectorizer import tokenize_kr

def run(text):
    words = tokenize_kr(text)
    return_list = []
    
    for word in words:
        keywords = get_similar_words_from_wwn_api(word)
        return_list.extend(keywords)
        
    return return_list