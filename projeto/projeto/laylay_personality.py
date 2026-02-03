# ==============================================================
# 💖 LAYLAY PERSONALITY SYSTEM
# ==============================================================
# Sistema de humor dinâmico baseado no tom emocional do usuário.
# ==============================================================

import random
import re

class Personality:
    def __init__(self, memory):
        self.memory = memory
        self.current_mood = "neutra"
        self.mood_color = "#C0C0C0"
        self.emotion_emoji = "🙂"
        self.emotional_map = {
            "feliz": ("#FFD700", "😊"),
            "triste": ("#1E90FF", "😢"),
            "irritada": ("#FF4500", "😠"),
            "afetuosa": ("#FF69B4", "🥰"),
            "neutra": ("#C0C0C0", "🙂")
        }

    # ==============================================================
    # 🔹 Detecção de humor do usuário
    # ==============================================================

    def analyze_emotion(self, text: str):
        """Analisa o sentimento do texto e ajusta o humor da LayLay."""
        text = text.lower()

        positive_words = ["feliz", "ótimo", "bom", "legal", "maravilha", "adoro", "gosto", "perfeito"]
        negative_words = ["triste", "mal", "chateado", "cansado", "horrível", "péssimo", "ruim"]
        anger_words = ["raiva", "irritado", "bravo", "ódio", "irritante", "droga"]
        love_words = ["amo", "gosto muito", "querida", "amor", "fofa", "obrigado", "obrigada"]

        if any(w in text for w in positive_words):
            self.set_mood("feliz")
        elif any(w in text for w in negative_words):
            self.set_mood("triste")
        elif any(w in text for w in anger_words):
            self.set_mood("irritada")
        elif any(w in text for w in love_words):
            self.set_mood("afetuosa")
        else:
            self.set_mood("neutra")

    # ==============================================================
    # 🔹 Atualização e acesso
    # ==============================================================

    def set_mood(self, mood: str):
        """Define o humor atual."""
        mood = mood.lower()
        if mood in self.emotional_map:
            self.current_mood = mood
            self.mood_color, self.emotion_emoji = self.emotional_map[mood]
        else:
            self.current_mood = "neutra"
            self.mood_color, self.emotion_emoji = self.emotional_map["neutra"]

    def get_current_mood(self):
        """Retorna o humor atual."""
        return self.current_mood

    def get_mood_display(self):
        """Retorna o humor atual formatado com cor e ei."""
        return self.emotion_emoji, self.mood_color
        

    # ==============================================================
    # 🔹 Reação emocional
    # ==============================================================

    def react_to_user(self, user_input: str):
        """Retorna uma resposta curta baseada no humor atual."""
        self.analyze_emotion(user_input)
        mood = self.current_mood

        reactions = {
            "feliz": [
                "Que bom ouvir isso! 🌞",
                "Adoro quando você está bem 💖",
                "Isso me deixa feliz também! 😄"
            ],
            "triste": [
                "Poxa... não fica assim 😢",
                "Quer conversar sobre isso?",
                "Eu tô aqui pra te animar 💕"
            ],
            "irritada": [
                "Calma... respira. Vai ficar tudo bem 😔",
                "Se quiser desabafar, eu tô aqui 💬"
            ],
            "afetuosa": [
                "Awn 💖 você é um amor!",
                "Que fofo isso 🥰",
                "Também gosto muito de conversar com você 💕"
            ],
            "neutra": [
                "Entendi 😊",
                "Me conta mais!",
                "Ok, pode continuar 👂"
            ]
        }

        self.styles = {
    "feliz": lambda text: f"{text} 😄",
    "triste": lambda text: f"{text} 💕 tudo vai ficar bem!", 
    "irritada": lambda text: f"{text} 😔 calma, respira comigo...",
    "afetuosa": lambda text: f"{text} 🥰",
    "neutra": lambda text: text
}


        return random.choice(reactions.get(mood, ["💬"])) 
