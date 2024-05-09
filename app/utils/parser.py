import re
import requests
from time import time
from bs4 import BeautifulSoup

from . import data

def get_dummy_sentence():
    sentence = "(서울=연합뉴스) 김잔디 오진송 권지현 기자 = '빅5'로 불리는 서울시내 주요 대형병원 중 서울대병원과 서울아산병원에 이어 나머지 병원도 주 1회 전면 휴진에 동참할 가능성이 커지고 있다."
    return sentence


def get_text_from_url(url):
    r = requests.get(url=url)

    text = None
    if r.status_code == 200:
        print(f"[{url}] url sent 200 code")        
        soup = BeautifulSoup(r.content, "html5lib")
        dic_area = soup.select_one("#dic_area")
        if dic_area is not None:
            text = dic_area.get_text()
            text = text.strip()
        else:
            print(f"dic_area not found on url = [{url}]")
    else:
        print(f"[{url}] url content not found")
    return text


# 1. '법' 검출 제외
# 2. '이태원참사 특별법' 같은 띄어쓰기 포함 법 검출
# 3. 중복으로 발견 시 CountVectorizer를 통한 나타나는 횟수 중요도 파악을 위해 중복 허용
def get_law_words_by_regex(text):
    text = text.strip()
    words = re.findall(r"[0-9가-힣]+법\b|'[0-9가-힣 ]+법'\b", text)
    words = [word.replace("'", "") if "'" in word else word for word in words] # quote removed
    
    # remove duplicates
    words = list(set(words))
    print(f"regex found {words}")
    return words


def get_law_words_by_json(text):
    result_list = []
    law_names = list(data.values())
    
    print("law name matching based on json begins")
    
    # search begins
    start = time()
    for name in law_names:
        if name in text:
            result_list.append(name)
            print(f"[{name}] found")
    end = time()
    
    # print timing
    duration = end - start
    prefix = "search spent "
    if duration >= 60:
        report_sentence = prefix + f"[{int(duration // 60)} minutes, {duration % 60 :.2f} seconds]"
    else:
        report_sentence = prefix + f"[{duration :.2f} seconds]"
    print(report_sentence)
    
    # remove duplicates
    result_list = list(set(result_list))
    return result_list
