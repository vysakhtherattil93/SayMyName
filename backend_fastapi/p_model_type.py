from pydantic import BaseModel
from typing import Literal

class Post(BaseModel):
    first_name: str
    last_name:str
    student_id : int
    lang_name: str = "en"
    course: str
    intake: Literal["Fall", "January", "May"]
    year: int


class Selection(BaseModel):
    student_id : int
    name:list
    name_selection: list
    votes: int
    show: bool