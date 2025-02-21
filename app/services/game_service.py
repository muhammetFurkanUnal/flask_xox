from ..game_engine.xoxEngine import Game
from ..services.ai_service.ai_service import AIService
import random


class GameService:

    def __init__(self):
        self.game = None
        self.ai_model:str = None
        self.pvp:bool = None
        self.turn:int = 1


    def startGame(self, pvp, ai_model, ai_player):
        self.ai_model = ai_model
        self.pvp = pvp
        self.game = Game()
        self.ai_service = AIService(self.ai_model, ai_player)
        
        if not pvp and ai_player == 1:
            self.move(random.randint(0,2), random.randint(0,2))


    def move(self, row, column):
        self.game.move(row, column)


    def getLog(self):
        return self.game.log
    
    
    
    
    