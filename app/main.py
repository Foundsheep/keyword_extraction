from fastapi import FastAPI
from .data_models.models import *
from .scripts import contexts_similarity, keywords_from_news, keywords_from_sentences, words_recommendation
import warnings
from .utils.util_keywords_extraction import get_law_words_by_regex, get_text_from_url

warnings.filterwarnings('ignore')

app = FastAPI()

@app.post("/url-keywords")
def get_keyword_from_url(info: News2Keywords):
    keywords_list = keywords_from_news.run(url_list=info.url_list,
                                 threshold=info.threshold,
                                 top_n=info.top_n)
    return keywords_list

@app.post("/sentence-keywords")
def get_keyword_from_sentences(info: Sentence2Keywords):
    keywords_list = keywords_from_sentences.run(text_list=info.text_list,
                                threshold=info.threshold,
                                top_n=info.top_n)
    return keywords_list

# TODO: threshold, top_n 
@app.post("/similar-words")
def get_similar_words_from_text(info: SimilarWords):
    words_list = words_recommendation.run(text=info.text)
    return words_list

@app.post("/similarity")
def get_similar_words_from_text(info: EmbeddingSimilarity):
    score = contexts_similarity.run(text_source=info.text_source,
                                    text_targets=info.text_targets)
    return score

