from ..utils.util_keywords_extraction import extract_keywords_by_keybert_with_law_names

def run(text_list, threshold=0.0, top_n=10):
    keywords_list = []
    for text in text_list:
        keywords = extract_keywords_by_keybert_with_law_names(text, top_n, threshold)

        # set to the output format
        concatenated_keywords = ",".join(keywords)
        keywords_list.append(concatenated_keywords)

    return keywords_list
