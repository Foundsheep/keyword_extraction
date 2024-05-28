from .kw_vectorizer import get_vectorizer
import json
import os
import urllib3

vectorizer = get_vectorizer()

# law_names.json에서 불러와서 메모리에 올리기
cur_dir = os.path.dirname(os.path.realpath(__file__))
print(f"{cur_dir = }")
file_name = "law_names.json"
json_path = os.path.join(cur_dir, file_name)
with open(json_path, "r") as f:
    data = json.load(f)
    print(f"law names are loaded successfully from {json_path}")


# PoolManager
http = urllib3.PoolManager()