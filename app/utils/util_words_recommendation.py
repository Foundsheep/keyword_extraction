from ..configuration import Config
from . import http
import json

def get_similar_words_from_wwn_api(word):

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

            return_list.extend(synonyms)
            print(f"synonyms for word[{word}] = {synonyms}")
            return_list.extend(hypernyms)
            print(f"hypernyms for word[{word}] = {hypernyms}")
            return_list.extend(hypornyms)
            print(f"hypornyms for word[{word}] = {hypornyms}")

            # 정제
            return_list = [w.split("_")[0] for w in return_list]

        else:
            print(f"call suceeded, but no words found in dictionary for word [{word}]")
    else:
        print(f"open api call failed. Call status = [{response.status}]")

    return return_list    