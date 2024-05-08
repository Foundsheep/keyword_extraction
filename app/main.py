from fastapi import FastAPI
from .models.key_bert import get_dummy_model, count_parameters, get_keybert
from .data_models.models import *
from .scripts import news2key

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}



@app.post("/url-keyword")
def get_keyword_from_url(info: News2Keywords):
    keywords_list = news2key.run(url_list=info.url_list,
                                 threshold=info.threshold,
                                 top_n=info.top_n)
    return keywords_list

@app.post("/sentence-keyword")
def get_keyword_from_sentences():
    return {"result": "OK"}