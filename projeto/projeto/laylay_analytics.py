# laylay_analytics.py

import time

class Analytics:
    """Classe simples para registrar e analisar interações do usuário."""

    def __init__(self):
        self.logs = []
    
    def log_interaction(self, user_input, response, response_time):
        """Salva uma interação com tempo de resposta."""
        self.logs.append({
            "user_input": user_input,
            "response": response,
            "response_time": response_time,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
    
    def get_summary(self):
        """Retorna um resumo básico das interações."""
        if not self.logs:
            return {"total_interactions": 0, "avg_response_time": 0.0}
        
        total_time = sum(log["response_time"] for log in self.logs)
        return {
            "total_interactions": len(self.logs),
            "avg_response_time": round(total_time / len(self.logs), 2)
        }
