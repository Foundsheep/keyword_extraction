import traceback
from ..utils.util_keywords_extraction import extract_keywords_by_keybert_with_law_names

def run(text_list, threshold=0.0, top_n=10):
    keywords_list = None
    try:
        keywords_list = []
        for text in text_list:
            keywords = extract_keywords_by_keybert_with_law_names(text, top_n, threshold)

            # set to the output format
            if len(keywords) != 0:
                concatenated_keywords = ",".join(keywords)
            else:
                concatenated_keywords = ""
            keywords_list.append(concatenated_keywords)
    except Exception as e:
        print(e)
        traceback.print_exc()
    return keywords_list
