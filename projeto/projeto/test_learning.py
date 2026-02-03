import sys
import os
import random
import json
from datetime import datetime

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock de st.session_state e st.error para simular o ambiente Streamlit
class MockSessionState:
    def __init__(self):
        self.memory = None
        self.personality = None
        self.analytics = None
        self.learning_system = None
        self.llm = MockLLM()
        self.knowledge = None
        self.emotions = None
        self.messages = []

class MockLLM:
    """Mock da LLM para simular a resposta de aprendizado."""
    def generate_response(self, system_prompt, messages):
        # Simula a extração de um fato pessoal
        if "meu nome é joão" in system_prompt.lower():
            return """
            ```json
            {
              "user_data": { "nome_usuario": "João" },
              "learned_facts": {}
            }
            ```
            """
        # Simula a extração de um fato geral
        elif "eu gosto de pizza" in system_prompt.lower():
            return """
            ```json
            {
              "user_data": {},
              "learned_facts": { "gosto_comida": "pizza" }
            }
            ```
            """
        # Simula nenhuma extração
        else:
            return "{}"

def mock_st_error(message):
    print(f"[MOCK_ST_ERROR]: {message}")

def mock_st_spinner(message):
    class Spinner:
        def __enter__(self):
            print(f"[MOCK_ST_SPINNER]: {message}")
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
    return Spinner()

# Substitui as dependências do Streamlit
sys.modules['streamlit'] = type('module', (object,), {
    'session_state': MockSessionState(),
    'error': mock_st_error,
    'spinner': mock_st_spinner,
    'set_page_config': lambda *args, **kwargs: None,
    'markdown': lambda *args, **kwargs: None,
    'columns': lambda *args, **kwargs: (type('col', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, *args: None}),)*2,
    'header': lambda *args, **kwargs: None,
    'subheader': lambda *args, **kwargs: None,
    'write': lambda *args, **kwargs: None,
    'text_input': lambda *args, **kwargs: None,
    'button': lambda *args, **kwargs: None,
    'chat_message': lambda *args, **kwargs: type('msg', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, *args: None})
})

# Importa os módulos após o mock
from laylay_learning_system import LearningSystem
from laylay_db import setup_database, get_db_connection

# Mock da função run_learning_step para testar a lógica de should_force_learn
def run_learning_step_mock(context: list, user_input: str, assistant_response: str, force_learn: bool = False):
    """Mock da função de aprendizado para verificar se foi chamada."""
    print(f"--- run_learning_step_mock chamado ---")
    print(f"User Input: {user_input}")
    print(f"Force Learn: {force_learn}")
    
    # Se force_learn for True, simula o processamento
    if force_learn:
        print("Processando aprendizado forçado...")
        # Simula a chamada ao process_learning_response
        llm_mock = MockLLM()
        learning_response = llm_mock.generate_response("system_prompt", context)
        
        # Simula o contexto da conversa
        context_messages = [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_response}
        ]
        
        # O LearningSystem precisa ser inicializado
        ls = LearningSystem()
        ls.process_learning_response(
            response_text=learning_response,
            context_messages=context_messages,
            user_input=user_input,
            assistant_response=assistant_response,
            force_learn=force_learn
        )
        print("Aprendizado forçado processado.")
    else:
        print("Aprendizado ignorado (chance de 90% para evitar Rate Limit).")
    print("--------------------------------------")

def test_learning_system():
    print("Iniciando Teste do Sistema de Aprendizado...")
    
    # 1. Configura o DB (garante que as tabelas estão corretas)
    setup_database()
    
    # 2. Inicializa o LearningSystem
    ls = LearningSystem()
    
    # 3. Simula interações
    
    # Caso 1: Aprendizado Forçado (Nome)
    user_input_1 = "Meu nome é João e eu sou desenvolvedor."
    assistant_response_1 = "Que nome lindo, João! Prazer em te conhecer."
    context_1 = [{"role": "user", "content": user_input_1}, {"role": "assistant", "content": assistant_response_1}]
    
    force_learn_1 = ls.should_force_learn(user_input_1)
    print(f"Teste 1 (Nome): Force Learn = {force_learn_1}")
    if force_learn_1:
        # Simula a chamada de aprendizado
        ls.process_learning_response(
            response_text="""{"user_data": {"nome_usuario": "João", "profissao": "desenvolvedor"}, "learned_facts": {}}""",
            context_messages=context_1,
            user_input=user_input_1,
            assistant_response=assistant_response_1,
            force_learn=True
        )
    
    # Caso 2: Aprendizado Forçado (Gosto)
    user_input_2 = "Eu gosto muito de pizza e de viajar."
    assistant_response_2 = "Pizza é maravilhoso! Qual seu destino favorito?"
    context_2 = [{"role": "user", "content": user_input_2}, {"role": "assistant", "content": assistant_response_2}]
    
    force_learn_2 = ls.should_force_learn(user_input_2)
    print(f"Teste 2 (Gosto): Force Learn = {force_learn_2}")
    if force_learn_2:
        # Simula a chamada de aprendizado
        ls.process_learning_response(
            response_text="""{"user_data": {"gosto_comida": "pizza"}, "learned_facts": {"gosto_geral": "viajar"}}""",
            context_messages=context_2,
            user_input=user_input_2,
            assistant_response=assistant_response_2,
            force_learn=True
        )
        
    # Caso 3: Aprendizado Não Forçado (Conversa trivial)
    user_input_3 = "O tempo está bom hoje, não acha?"
    force_learn_3 = ls.should_force_learn(user_input_3)
    print(f"Teste 3 (Trivial): Force Learn = {force_learn_3}")
    
    # 4. Verifica os resultados no DB
    print("\n--- Verificação do Banco de Dados ---")
    user_data = ls.get_user_data()
    print(f"User Data: {user_data}")
    
    facts_string = ls.get_all_facts_as_string()
    print(f"\nFatos para Prompt:\n{facts_string}")
    
    # Verifica se o contexto foi salvo
    conn = get_db_connection()
    cursor = conn.execute("SELECT fact, context FROM user_facts")
    
    print("\nFatos com Contexto:")
    for row in cursor:
        print(f"Fato: {row['fact']}")
        # Tenta carregar o JSON do contexto
        try:
            context_loaded = json.loads(row['context'])
            print(f"Contexto (JSON): {context_loaded}")
        except Exception as e:
            print(f"Erro ao carregar contexto JSON: {e}")
        print("-" * 20)
        
    conn.close()
    
    # 5. Verifica a Validação de Conflitos (user_data)
    # Simula a mudança de nome
    user_input_4 = "Na verdade, meu nome é Pedro."
    assistant_response_4 = "Ah, Pedro! Desculpe a confusão."
    context_4 = [{"role": "user", "content": user_input_4}, {"role": "assistant", "content": assistant_response_4}]
    
    ls.process_learning_response(
        response_text="""{"user_data": {"nome_usuario": "Pedro"}, "learned_facts": {}}""",
        context_messages=context_4,
        user_input=user_input_4,
        assistant_response=assistant_response_4,
        force_learn=True
    )
    
    print("\n--- Verificação de Conflito (Nome) ---")
    user_data_final = ls.get_user_data()
    print(f"User Data Final: {user_data_final}")
    assert user_data_final.get('nome_usuario') == 'Pedro', "Falha na validação de conflito (INSERT OR REPLACE)"
    
    print("\nTeste Concluído com Sucesso!")

if __name__ == "__main__":
    # Garante que o DB de teste está limpo
    if os.path.exists(Config.DB_NAME):
        os.remove(Config.DB_NAME)
        
    # Mock da Config para usar um DB de teste
    class Config:
        DB_NAME = "laylay_test_memory.db"
        DB_TIMEOUT = 10.0
        MAX_CONTEXT = 15
        CACHE_SIZE = 100
        SENTIMENT_THRESHOLD = 0.5
        EMOTION_DECAY_RATE = 0.95
        EMOTION_UPDATE_FACTOR = 0.2
        RESPONSE_TIMEOUT = 5.0
        PERSONALITY_TRAITS = {}
        
    # Substitui a Config original
    sys.modules['laylay_config'] = type('module', (object,), {'Config': Config})
    
    test_learning_system()
