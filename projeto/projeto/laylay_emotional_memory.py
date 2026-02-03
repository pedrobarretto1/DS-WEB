import sqlite3
from datetime import datetime
from laylay_config import Config # Importar Config

class EmotionalMemory:
    def __init__(self, db_path=Config.DB_NAME): # Usar o DB_NAME do Config
        self.db_path = db_path
        self._setup_db()

    def _setup_db(self):
        # A função de setup agora está centralizada no laylay_db.py
        # Podemos apenas garantir a conexão
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("SELECT 1 FROM emotions LIMIT 1") # Apenas testa se a tabela existe
            conn.close()
        except Exception as e:
            # Se falhar, o setup_database() principal ainda não rodou
            # ou está com erro.
            print(f"Aguardando setup_database() centralizado: {e}")
            pass # A tabela será criada pelo laylay_db.py

    def save_emotion(self, emotion):
        conn = sqlite3.connect(self.db_path)
        
        # CORREÇÃO AQUI: Especificamos as colunas (timestamp, emotion)
        # O 'id' será preenchido automaticamente pelo AUTOINCREMENT.
        conn.execute(
            "INSERT INTO emotions (timestamp, emotion) VALUES (?, ?)", 
            (datetime.now().isoformat(), emotion)
        )
        
        conn.commit()
        conn.close()

    def last_emotion(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute("SELECT emotion FROM emotions ORDER BY timestamp DESC LIMIT 1")
        result = cur.fetchone()
        conn.close()
        return result[0] if result else None