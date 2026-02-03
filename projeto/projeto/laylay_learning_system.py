# laylay_learning_system.py
# laylay_learning_system.py

import json
import sqlite3
from datetime import datetime
# Importamos as funções do DB para gerenciarmos a persistência
from laylay_db import get_db_connection, safe_db_operation

class LearningSystem:
    """Sistema de aprendizado e persistência de memória da LayLay."""

    def __init__(self):
        # O __init__ agora apenas inicializa, a persistência é no DB.
        pass

    def should_force_learn(self, user_input: str) -> bool:
        """
        Verifica se a entrada do usuário contém frases-chave que indicam
        informação pessoal que deve ser aprendida imediatamente.
        """
        user_input_lower = user_input.lower()
        
        # Padrões comuns para informações pessoais
        patterns = [
            "meu nome é", "eu sou o", "eu sou a",
            "eu gosto de", "eu amo", "meu hobby é",
            "eu tenho [0-9]+ anos", "minha idade é",
            "eu moro em", "minha cidade é",
            "meu trabalho é", "eu sou [a-z]+",
            "eu tenho um pet", "meu pet é",
            "minha família", "meu filho", "minha filha",
            "eu odeio", "eu não gosto de"
        ]
        
        for pattern in patterns:
            # Para padrões com números, usamos uma verificação mais simples por enquanto
            if "[0-9]+" in pattern:
                if any(word.isdigit() for word in user_input_lower.split()) and pattern.replace("[0-9]+", "").strip() in user_input_lower:
                    return True
            elif pattern in user_input_lower:
                return True
                
        return False
    
    @safe_db_operation
    def process_learning_response(self, response_text: str, context_messages: list, user_input: str, assistant_response: str, force_learn: bool):
        """
        Analisa o JSON da LLM de aprendizado e salva os fatos no banco de dados.
        """
        try:
            # 1. Tenta limpar e carregar o JSON
            cleaned_text = response_text.strip().replace("```json", "").replace("```", "").strip()
            
            # Se a resposta foi um erro (ex: RateLimitError tratado no LLM), o JSON será inválido
            if cleaned_text.startswith("⚠️ Ops!"):
                print(f"[Memória]: Resposta de aprendizado veio com erro e não será processada: {cleaned_text}")
                return

            if not cleaned_text:
                print("[Memória]: Resposta de aprendizado da LLM estava vazia.")
                return

            data = json.loads(cleaned_text)

            conn = get_db_connection()
            cursor = conn.cursor()
            timestamp = datetime.now().timestamp()
            
            # Converte o contexto da conversa para JSON para salvar
            context_json = json.dumps(context_messages)
            
            # 2. Salva Dados do Usuário (user_data table: key, value)
            # Ex: nome_usuario, idade, etc.
            user_data = data.get("user_data", {})
            for key, value in user_data.items():
                if key and value:
                    # Usamos INSERT OR REPLACE para garantir que o dado mais novo seja sempre salvo
                    cursor.execute("""
                        INSERT OR REPLACE INTO user_data (key, value) VALUES (?, ?)
                    """, (key, str(value)))

            # 3. Salva Fatos Aprendidos (user_facts table: category, fact, timestamp)
            # Ex: memórias específicas de conversas
            learned_facts = data.get("learned_facts", {})
            for key, value in learned_facts.items():
                if key and value:
                    # 4. Validação de Dados (Simples: Verifica se o fato já existe)
                    # Se o fato for um user_data, ele já é tratado com REPLACE.
                    # Para user_facts, vamos verificar se já existe um fato muito similar.
                    # Por enquanto, mantemos o INSERT OR IGNORE, mas adicionamos o contexto.
                    
                    # Usamos INSERT OR IGNORE para evitar salvar o MESMO fato repetidamente
                    try:
                        # 4. Validação de Dados: O UNIQUE(category, fact) já previne duplicatas exatas.
                        # Para conflitos em user_data, o INSERT OR REPLACE já garante que o dado mais novo prevaleça.
                        cursor.execute("""
                            INSERT OR IGNORE INTO user_facts (category, fact, timestamp, context) VALUES (?, ?, ?, ?)
                        """, (key, str(value), timestamp, context_json))
                    except sqlite3.IntegrityError:
                        # Ocorre se UNIQUE(category, fact) falhar (duplicata)
                        pass 

            conn.commit()
            conn.close()
            print("[Memória]: Fatos aprendidos e salvos com sucesso.")

        except json.JSONDecodeError as e:
            print(f"[Memória]: Resposta de aprendizado da LLM não era um JSON válido: {response_text}. Erro: {e}")
        except Exception as e:
            print(f"[Memória]: Erro inesperado ao processar a resposta de aprendizado: {e}")


    @safe_db_operation
    def get_user_data(self) -> dict:
        """
        Retorna todos os dados simples do usuário (nome, etc.) da tabela user_data.
        (Implementado para corrigir o AttributeError)
        """
        conn = get_db_connection()
        cursor = conn.execute("SELECT key, value FROM user_data")
        
        user_data = {row['key']: row['value'] for row in cursor}
        
        conn.close()
        return user_data

    @safe_db_operation
    def get_all_facts_as_string(self) -> str:
        """
        Compila todos os fatos aprendidos (user_data e user_facts) em uma string formatada
        para ser incluída no System Prompt da LLM.
        """
        facts = []
        
        # 1. Recupera user_data (fatos simples)
        user_data = self.get_user_data()
        for key, value in user_data.items():
            facts.append(f"DADO USUÁRIO: {key.replace('_', ' ').title()}: {value}")

        # 2. Recupera user_facts (memórias complexas)
        conn = get_db_connection()
        # Seleciona os 10 fatos mais recentes e relevantes
        cursor = conn.execute("""
            SELECT category, fact, timestamp 
            FROM user_facts 
            ORDER BY timestamp DESC 
            LIMIT 10
        """) 
        
        for row in cursor:
            # Formato: CATEGORIA [timestamp]: fato
            facts.append(f"MEMÓRIA: {row['category'].title()}: {row['fact']}")
            
        conn.close()
        
        if not facts:
            return "Nenhum fato relevante foi aprendido ainda. Comece a conversar!"
            
        return "\n".join(facts)