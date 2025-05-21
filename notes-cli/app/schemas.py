from typing import Optional
from pydantic import BaseModel


class NotesIn(BaseModel):
    title: str
    content: Optional[str] = None

class NotesOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes =  True