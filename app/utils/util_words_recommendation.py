from ..configuration import Config
from . import http
import json

import hashlib
import hmac
import base64

import time
import requests

def get_similar_words_from_wwn_api(word, top_n):

    print(f"word to api : [{word}]")
    return_list = []

    # info setting
    request_json = {
        "argument": {
            "word": word
        }
    }
    response = http.request(
        "POST",
        Config.OPEN_API_URL,
        headers={"Content-Type": "application/json; charset=UTF-8","Authorization" :  Config.KR_WISE_WORD_NET_API_KEY},
        body=json.dumps(request_json)
    )

    if response.status == 200:
        j = json.loads(response.data.decode("utf-8"))
        candidate_list = j["return_object"]["WWN WordInfo"]

        # 사전에 있는 단어이면
        if len(candidate_list) > 0:
            for candidate in candidate_list:
                synonyms = candidate["Synonym"]
                hypernyms = []
                hypornyms = []
                word_info_list = candidate["WordInfo"]
                for word_info in word_info_list:
                    hypernyms.extend(word_info["Hypernym"])
                    hypornyms.extend(word_info["Hypornym"])

            # 1단계 유사어
            return_list.extend(synonyms[:top_n])
            print(f"synonyms for word[{word}] = {synonyms[:top_n]}")

            # 2단계 상위어
            if len(return_list) < top_n:
                new_top_n = top_n - len(return_list)
                return_list.extend(hypernyms[:new_top_n])
                print(f"hypernyms for word[{word}] = {hypernyms[:new_top_n]}")
            
            # 3단계 하위어
            if len(return_list) < top_n:
                new_top_n = top_n - len(return_list)
                return_list.extend(hypornyms[:new_top_n])
                print(f"hypornyms for word[{word}] = {hypornyms[:new_top_n]}")

            # 정제
            return_list = [w.split("_")[0] for w in return_list]

        else:
            print(f"call suceeded, but no words found in dictionary for word [{word}]")
    else:
        print(f"open api call failed. Call status = [{response.status}]")

    return return_list    


# naver api 활용을 위한 클래스
class Signature:

    @staticmethod
    def generate(timestamp, method, uri, secret_key):
        message = "{}.{}.{}".format(timestamp, method, uri)
        hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)

        hash.hexdigest()
        return base64.b64encode(hash.digest())

def get_similar_words_from_naver_ad_api(word, top_n=10):

    def _get_header(method, uri, api_key, secret_key, customer_id):
        timestamp = str(round(time.time() * 1000))
        signature = Signature.generate(timestamp, method, uri, Config.NAVER_SECRET_KEY)
        return {
            'Content-Type': 'application/json; charset=UTF-8', 
            'X-Timestamp': timestamp, 
            'X-API-KEY': Config.NAVER_API_KEY, 
            'X-Customer': str(Config.NAVER_CUSTOMER_ID), 
            'X-Signature': signature
            }
    
    return_list = []

    method = 'GET'

    params={}
    params['hintKeywords']=word
    params['showDetail']='1'

    r=requests.get(Config.NAVER_BASE_URL + Config.NAVER_URI, 
                   params=params, 
                   headers=_get_header(method, 
                                       Config.NAVER_URI, 
                                       Config.NAVER_API_KEY,
                                       Config.NAVER_SECRET_KEY,
                                       Config.NAVER_CUSTOMER_ID))

    if r.status_code == 200:
        print(f"naver api call suceeded")

        j = r.json()
        keywords = j["keywordList"][1:] # 본인 단어는 제외
        try:
            for i in range(top_n):
                rel_keyword = keywords[i]["relKeyword"]
                return_list.append(rel_keyword)
        except Exception as e:
            print(e)
            print(f"[{i+1}]th element caused an error. {len(return_list) = }")
    
    else:
        print(f"{r.status_code = }")
    
    return return_list