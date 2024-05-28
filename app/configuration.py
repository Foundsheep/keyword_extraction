from dataclasses import dataclass

@dataclass
class Config:
    # KR_DICT_API_KEY: str = "E46D906ADBB4387D1E4EFCD343F2D489"

    # https://aiopen.etri.re.kr/guide/Word
    KR_WISE_WORD_NET_API_KEY = "ee1810c8-dc20-4698-8208-1c5adb7fe4b9"
    OPEN_API_URL = "http://aiopen.etri.re.kr:8000/WiseWWN/Word"