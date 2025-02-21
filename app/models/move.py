from pydantic import BaseModel

class Move(BaseModel):
    row:int
    column:int
    