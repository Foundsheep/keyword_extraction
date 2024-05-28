from ..utils.util_keywords_extraction import extract_keywords_by_keybert_with_law_names, get_text_from_url

def run(url_list, threshold=0.0, top_n=10):
    keywords_list = []
    for url in url_list:
        print(f"{url = }")

        # TODO: try, except to catch the url provided doesn't match the naver news html structure
        text = get_text_from_url(url)
        keywords = extract_keywords_by_keybert_with_law_names(text, top_n, threshold)

        # set to the output format
        concatenated_keywords = ",".join(keywords)
        keywords_list.append(concatenated_keywords)

    return keywords_list
