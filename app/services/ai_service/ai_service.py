import joblib
from ...config import *
import numpy as np

class AIService:
    
    def __init__(self, ai_model_name, ai_player):
        if ai_model_name == MLP and ai_player == 1:
            self.ai_model = joblib.load('app/services/ai_service/models/mlp_X_model.pkl')
    
        elif ai_model_name == MLP and ai_player == 2:
            self.ai_model = joblib.load('app/services/ai_service/models/mlp_O_model.pkl')
            
            
    def predict(self, flat_board):
        
        y_pred = [np.array(flat_board)]
        y_pred_proba = self.ai_model.predict_proba(y_pred)[0]
        
        while True:
            y_pred = np.argmax(y_pred_proba)
            # check if played location is empty, otherwise play next most possible location
            if (flat_board[y_pred] != 0):
                y_pred_proba[y_pred] = 0
            else:
                break
            
        
        row = y_pred // 3
        column = y_pred % 3
        
        return (row, column)
          
    

