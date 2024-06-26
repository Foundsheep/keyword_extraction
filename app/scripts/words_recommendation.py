import traceback
import numpy as np

from ..utils.util_keywords_extraction import tokenize_kr
from ..utils.util_words_recommendation import get_similar_words_from_naver_ad_api, get_similar_words_from_wwn_api
from . import contexts_similarity as cs

def run(text, threshold=0.3, top_n=10):
    return_list = None
    try:
        # 하나의 문장 형태로 들어온다면 tokenize
        if len(text.strip().split()) > 1:
            print(f"input text has more than 1 word, length = {len(text.strip().split())}")
            tokens = tokenize_kr(text)
            
            # 의미 있는 단어만 선별
            print(f"1nd stage... {len(tokens) = }")

            scores = cs.run([text], tokens)
            scores = np.array(scores)
            indices = np.where(scores >= threshold)[0]
            tokens_arr = np.array(tokens)
            words = list(tokens_arr[indices])

            print(f"After 1nd stage... {len(words) = }")
        else:
            words = [text]

        # 아무리 많아도 3개까지만 탐색
        words = words[:3]

        # API를 통한 추천 단어 추출
        keyword_list = []
        
        # word 별로 top_n * 2개씩 추출
        for word in words:
            print(f"{word = }")
            naver_keywords = get_similar_words_from_naver_ad_api(word, top_n)
            print(f"naver... {len(naver_keywords) = }")
            keyword_list.extend(naver_keywords)

            wwn_keywords = get_similar_words_from_wwn_api(word, top_n)
            print(f"wwn... {len(wwn_keywords) = }")
            keyword_list.extend(wwn_keywords)

        print(f"2nd stage... {len(keyword_list) = }")

        # 유사도 기반으로 적합한 것만 추출
        scores_final = cs.run([text], keyword_list)
        scores_final = np.array(scores_final)
        indices_final = np.where(scores_final >= threshold)[0]
        tokens_arr_final = np.array(keyword_list)
        return_list = list(tokens_arr_final[indices_final])

        print(f"After 2nd stage... {len(return_list) = }")

        # top_n 개만 추출
        return_list = return_list[:top_n]
    
    except Exception as e:
        print(e)
        traceback.print_exc()
    return return_list

