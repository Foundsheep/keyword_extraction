from ..configuration import Config
from . import http
import json

def get_similar_words_from_wwn_api(word):

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
        candidates = ["return_object"]["WWN WordInfo"]

        # 사전에 있는 단어이면
        if len(candidates) > 0:
            for candidate in candidate:
                synonyms = candidate["Synonym"]
                hypernums = []
                hypornums = []
                word_info_list = candidate["WordInfo"]
                for word_info in word_info_list:
                    hypernums.extend(word_info["Hypernym"])
                    hypornums.extend(word_info["Hypornum"])

            return_list.extend(synonyms)
            return_list.extend(hypernums)
            return_list.extend(hypornums)

            # 정제
            return_list = [w.split("_")[0] for w in return_list]

        else:
            print(f"call suceeded, but no words found in dictionary for word [{word}]")
    else:
        print(f"open api call failed. Call status = [{response.status}]")

    return return_list    