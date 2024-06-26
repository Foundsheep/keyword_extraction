from pydantic import BaseModel
from typing import Union, List

class News2Keywords(BaseModel):
    url_list: Union[List[str], None] = None
    threshold: float = 0.0
    top_n: int = 10

class Sentence2Keywords(BaseModel):
    text_list: Union[List[str], None] = None
    threshold: float = 0.0
    top_n: int = 10

class SimilarWords(BaseModel):
    text: str = None
    threshold: float = 0.5
    top_n: int = 10

class EmbeddingSimilarity(BaseModel):
    text_source: Union[List[str], None] = None
    text_targets: Union[List[str], None] = None