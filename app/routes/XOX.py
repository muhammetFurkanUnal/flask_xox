from flask import Blueprint, jsonify, request, session
from ..services.game_service import GameService
from ..models import Start_game, Move


XOX_engine_BP = Blueprint("XOX_engine_BP", __name__)
gameService = GameService()


@XOX_engine_BP.route("/start", methods=["POST"])
def route_start():
    data = request.get_json()
    # get request as a model object using pydantic
    data = Start_game(**data)
    
    gameService.startGame(data.pvp, data.ai_model, data.ai_player)
    return jsonify(gameService.getLog())



@XOX_engine_BP.route("/move", methods=["POST"])
def route_move():
    data = request.get_json()
    
    gameService.move(data["row"], data["column"])
    
    if gameService.getLog()["winner"] != 0:
        return jsonify(gameService.getLog())
    
    if gameService.pvp == False:
        (row, column) = gameService.ai_service.predict(gameService.getLog()["flat_board"])
        gameService.move(row, column)
    
    return jsonify(gameService.getLog())

