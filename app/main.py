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
    url_list = info.url_list
    keywords_list = news2key.run(url_list=url_list)
    return keywords_list

@app.post("/sentence-keyword")
def get_keyword_from_sentences():
    return {"result": "OK"}