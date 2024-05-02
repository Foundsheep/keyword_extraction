from pydantic import BaseModel
from typing import Union, List

class News2Keywords(BaseModel):
    url_list: Union[List[str], None] = None