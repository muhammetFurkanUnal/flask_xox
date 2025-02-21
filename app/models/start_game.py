from pydantic import BaseModel

class Start_game(BaseModel):
    ai_model:str
    pvp: bool
    ai_player:int
    