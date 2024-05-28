from fastapi import FastAPI
from .data_models.models import *
from .scripts import news2key, sen2key, word_recommend

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.post("/url-keywords")
def get_keyword_from_url(info: News2Keywords):
    keywords_list = news2key.run(url_list=info.url_list,
                                 threshold=info.threshold,
                                 top_n=info.top_n)
    return keywords_list

@app.post("/sentence-keywords")
def get_keyword_from_sentences(info: Sentence2Keywords):
    keywords_list = sen2key.run(text_list=info.text_list,
                                threshold=info.threshold,
                                top_n=info.top_n)
    return keywords_list

@app.post("/similar-words")
def get_similar_words_from_text(info: SimilarWords):
    words_list = word_recommend.run(text=info.text)
    return words_list
