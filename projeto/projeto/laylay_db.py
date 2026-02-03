import sqlite3
import streamlit as st
from laylay_config import Config

# ============================================================================
# FUNÇÕES DE BANCO DE DADOS
# ============================================================================

def safe_db_operation(func):
    """Decorator para operações seguras no banco de dados com tratamento de erro."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            # Em um ambiente Streamlit, é bom usar st.error para feedback visual
            st.error(f"Erro no banco de dados: {e}")
            # Logar o erro para debug seria ideal aqui
            print(f"Erro no banco de dados: {e}") # Adicionado print para debug
            return None
        except Exception as e:
            st.error(f"Erro inesperado durante operação de DB: {e}")
            print(f"Erro inesperado durante operação de DB: {e}") # Adicionado print para debug
            return None
    return wrapper

def get_db_connection():
    """Cria e retorna a conexão com o banco de dados SQLite com timeout otimizado."""
    # Usando Config.DB_NAME e Config.DB_TIMEOUT
    conn = sqlite3.connect(Config.DB_NAME, timeout=Config.DB_TIMEOUT, isolation_level=None)
    conn.row_factory = sqlite3.Row
    # Ativar WAL mode para melhor performance em concorrência
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn

@safe_db_operation
def setup_database():
    """Configura as tabelas iniciais no banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Tabela para dados do usuário (nome, interesses, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    
    # Tabela para o estado interno da IA (emoções, humor, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ia_state (
            key TEXT PRIMARY KEY,
            value REAL
        )
    """)
    
    # Tabela para fatos aprendidos (memória de longo prazo)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learned_facts (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    
    # Tabela para fatos aprendidos com categoria e timestamp (melhor estrutura)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_facts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            fact TEXT,
            timestamp REAL,
            context TEXT, -- Nova coluna para armazenar o contexto da conversa
            UNIQUE(category, fact)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            emotion TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Chamada inicial para garantir que o DB esteja pronto
setup_database()

def upgrade_database():
    """Adiciona coluna context se não existir"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar se coluna context existe
    cursor.execute("PRAGMA table_info(user_facts)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'context' not in columns:
        cursor.execute("ALTER TABLE user_facts ADD COLUMN context TEXT")
        conn.commit()
        print("✅ Coluna 'context' adicionada com sucesso!")
    
    conn.close()

# Executar atualização
upgrade_database()