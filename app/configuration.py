from dataclasses import dataclass

@dataclass
class Config:
    # https://aiopen.etri.re.kr/guide/Word
    KR_WISE_WORD_NET_API_KEY = "ee1810c8-dc20-4698-8208-1c5adb7fe4b9"
    OPEN_API_URL = "http://aiopen.etri.re.kr:8000/WiseWWN/Word"
    NAVER_BASE_URL = 'https://api.searchad.naver.com'
    NAVER_URI = '/keywordstool'

    # https://yenpa.tistory.com/11
    NAVER_API_KEY = '01000000007d0e897d57e7af5bb1a4222e54870198a42d10e6a2f5ed3bb3a1adbacd5bea4c'
    NAVER_SECRET_KEY = 'AQAAAAB9Dol9V+evW7GkIi5UhwGY29uIyBvHW4+EKuFc05Zq2A=='
    NAVER_CUSTOMER_ID = '1801275'