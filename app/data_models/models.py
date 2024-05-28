from pydantic import BaseModel
from typing import Union, List

class News2Keywords(BaseModel):
    url_list: Union[List[str], None] = None
    threshold: float = None
    top_n: int = None

class Sentence2Keywords(BaseModel):
    text_list: Union[List[str], None] = None
    threshold: float = None
    top_n: int = None

class SimilarWords(BaseModel):
    text: str = None

class EmbeddingSimilarity(BaseModel):
    text_1: str = None
    text_2: str = None