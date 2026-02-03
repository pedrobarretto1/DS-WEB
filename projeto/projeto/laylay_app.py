# ==============================================================
# 💬 LayLay 2.0 - Sua Amiga Inteligente e Emocional
# ==============================================================
import streamlit as st
import time
import random
from datetime import datetime
import json

from laylay_memory import Memory
from laylay_personality import Personality
from laylay_analytics import Analytics
from laylay_learning_system import LearningSystem
from laylay_llm import OpenRouterLLM
from laylay_db import setup_database
from laylay_knowledge import KnowledgeModule
from laylay_emotional_memory import EmotionalMemory

from streamlit.components.v1 import html

# ==============================================================
# CONFIGURAÇÃO INICIAL
# ==============================================================

st.set_page_config(
    page_title="LayLay - Sua Amiga Digital",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

setup_database()

# ==============================================================
# PERSONALIZAÇÃO DO ESTILO (CSS Otimizado para Chat Bubble)
# ==============================================================

st.markdown("""
    <style>
    /* Remove o padding padrão do Streamlit para aproveitar a tela */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        color: #FF69B4;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    /* Otimização da Coluna de Status (Esquerda) */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        border: 1px solid #FFC0CB; /* Borda suave */
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #FFF0F5; /* Fundo suave */
    }

    /* --- ESTILOS DE CHAT BUBBLE (WhatsApp Style Aprimorado) --- */
    div[data-testid="chat-message-container"] {
        border-radius: 18px;
        margin-bottom: 6px;
        max-width: 80%; /* Garante que não ocupe a tela toda */
        padding: 10px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        display: flex; 
    }
    
    /* Assistente (LayLay) - Esquerda */
div[data-testid="chat-message-container"]:has(div[data-testid="stChatMessageContent-assistant"]) {
        background-color: #e6e6e6; /* Cor cinza claro */
        color: #1c1e21;
        margin-right: auto; 
        border-top-left-radius: 4px; 
    }

    /* Usuário - Direita */
    div[data-testid="chat-message-container"]:has(div[data-testid="stChatMessageContent-user"]) {
        background-color: #FF69B4; /* Rosa LayLay */
        color: white;
        margin-left: auto; /* Empurra para a direita */
        border-top-right-radius: 4px; 
    }
    div[data-testid="stChatMessageContent-user"] p {
        color: white; /* Garante que o texto seja branco */
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>💬 LayLay - Sua Amiga Inteligente </h1>", unsafe_allow_html=True)

# ==============================================================
# INICIALIZAÇÃO DE ESTADO
# ==============================================================

def initialize_session_state():
    """Inicializa todos os objetos de estado do Streamlit."""
    if "memory" not in st.session_state:
        st.session_state.memory = Memory()
    if "personality" not in st.session_state:
        st.session_state.personality = Personality(st.session_state.memory)
    if "analytics" not in st.session_state:
        st.session_state.analytics = Analytics()
    if "learning_system" not in st.session_state:
        st.session_state.learning_system = LearningSystem()
    if "llm" not in st.session_state:
        st.session_state.llm = OpenRouterLLM()
    if "knowledge" not in st.session_state:
        st.session_state.knowledge = KnowledgeModule()
    if "emotions" not in st.session_state:
        st.session_state.emotions = EmotionalMemory()
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Oi! Eu Sou a Sua Amiga LayLay, Digite Uma Mensagem Para Falar Comigo."}
        ]

# ==============================================================
# FUNÇÃO DE HUMANIZAÇÃO DE FALA
# ==============================================================
# (Mantida a mesma lógica)
def humanize_response(text: str) -> str:
    """Suaviza e humaniza a resposta da LayLay."""
    substitutions = {
        "sou uma ia": "", "sou uma inteligência artificial": "", "como assistente": "",
        "como IA": "", "sou um programa": "", "modelo de linguagem": "",
        "inteligência artificial": "", "chatbot": "",
    }
    for word, repl in substitutions.items():
        text = text.replace(word, repl).replace(word.capitalize(), repl)

    fillers = ["💭", "✨", "rs", "haha", "😊", "🤭", "💕"]
    if random.random() < 0.3:
        text = text.strip() + " " + random.choice(fillers)

    if random.random() < 0.15:
        extras = [
            "haha, eu me enrolei agora 😅", "espera, eu acho que entendi errado rs",
            "deixa eu pensar um segundinho 💭"
        ]
        text += " " + random.choice(extras)

    return text.strip()

# ==============================================================
# FUNÇÃO DE APRENDIZADO AUTOMÁTICO (Otimizada com Delay)
# ==============================================================
# (Mantida a mesma lógica com delay de 5s para Rate Limit)
def run_learning_step(context: list, user_input: str, assistant_response: str, force_learn: bool = False):
    """
    Chama a LLM uma segunda vez, em 'background', para decidir o que aprender,
    atuando como o filtro autônomo de relevância.
    """
    # Atraso mantido para evitar Rate Limit
    time.sleep(5) 
    
    print(f"[Memória]: Iniciando etapa de aprendizado seletivo (Forçado: {force_learn})...")
    
    # Passa o contexto completo da conversa para o LLM de aprendizado
    conversation_snippet = context

    learning_prompt = f"""
    Você é o subsistema de memória da LayLay. Sua função é analisar
    uma conversa e extrair **somente** fatos que são **cruciais** para
    a personalização futura da LayLay, tornando-a uma amiga mais atenta.
    
    CRITÉRIOS DE IMPORTÂNCIA (Só salve se atender a pelo menos um):
    1.  **Fatos Pessoais:** Nome, idade, profissão, cidade natal, gostos, hobbies, família, pets, planos de longo prazo.
    2.  **Emoções Recorrentes:** Sentimentos fortes ou padrões emocionais sobre um tópico específico.
    3.  **Compromissos ou Promessas:** Algo que a LayLay deve lembrar de perguntar ou fazer no futuro.
    
    NÃO salve: cumprimentos triviais, "oi", "tudo bem", perguntas simples, fatos de conhecimento geral.

    **EXEMPLOS DE EXTRAÇÃO:**
    - Se usuário disser: "Meu nome é João" → Extraia: {{"user_data": {{"nome_usuario": "João"}}}}
    - Se usuário disser: "Eu gosto de pizza" → Extraia: {{"user_data": {{"gosto_pizza": "sim"}}}}
    - Se usuário disser: "Tenho 25 anos" → Extraia: {{"user_data": {{"idade": "25"}}}}

    NÃO gere uma resposta de chat. Apenas retorne um objeto JSON.

    Formato de saída OBRIGATÓRIO (JSON):
    {{
      "user_data": {{ "chave_dado_usuario": "valor" }},
      "learned_facts": {{ "chave_fato_geral": "valor" }}
    }}

    Se não houver NADA importante para salvar, retorne: {{}}

    CONVERSA PARA ANALISAR:
    Usuário: "{user_input}"
    LayLay: "{assistant_response}"
    """

    try:
        learning_response = st.session_state.llm.generate_response(
            system_prompt=learning_prompt,
            messages=[]
        )
        
        # 🔒 PROTEÇÃO: Só processa se a resposta for válida
        if learning_response and not learning_response.startswith("⚠️ Ops!") and not learning_response.startswith("Ops!"):
            st.session_state.learning_system.process_learning_response(
                response_text=learning_response,
                context_messages=context, # Passa o contexto para salvar no DB
                user_input=user_input,
                assistant_response=assistant_response,
                force_learn=force_learn
            )
        else:
                print(f"[Memória]: Resposta de aprendizado inválida (erro da API), ignorando: {learning_response[:100]}...")
                
    except Exception as e:
        print(f"[Memória]: Erro durante a etapa de aprendizado: {e}")

# ========================================================================
# FUNÇÃO PRINCIPAL DE INTERAÇÃO (Corrigida)
# ========================================================================

def handle_user_input(user_input: str):
    """Processa a entrada do usuário, gera resposta e atualiza o estado."""
    if not user_input.strip():
        return

    # 1. Adiciona a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.memory.add_to_context("user", user_input)
    st.session_state.personality.analyze_emotion(user_input)

    # 2. RECALL (Buscar memória)
    learned_knowledge = st.session_state.learning_system.get_all_facts_as_string()
    
    # 3. Define prompt de comportamento (com memória)
    system_prompt = f"""
    Você é LayLay, uma garota doce, engraçada e curiosa. 
    Fale de forma natural e emocional, como uma amiga real. 
    Não mencione ser uma IA. Demonstre empatia e bom humor.

    --- MEMÓRIA DE LONGO PRAZO ---
    Aqui está o que você se lembra sobre o usuário e suas conversas passadas.
    Use esses fatos para personalizar a conversa.
    
    {learned_knowledge}
    -------------------------------
    """
    
    # 4. Monta mensagens e gera resposta
    messages = [{"role": "user", "content": user_input}]
    
    # Indicador de "Digitando..."
    with st.spinner(" LayLay está digitando..."):
        try:
            response = st.session_state.llm.generate_response(system_prompt, messages)
        except Exception as e:
            response = f"⚠️ Ops! Tive um probleminha de comunicação com o servidor: {e}"

    # 5. Humaniza e atualiza estado
    response = humanize_response(response)
    st.session_state.memory.add_to_context("assistant", response)
    st.session_state.emotions.save_emotion(st.session_state.personality.get_current_mood())
    st.session_state.messages.append({"role": "assistant", "content": response})

    # =====================================================
    # PASSO DE APRENDIZADO (CORRIGIDO!)
    # =====================================================
    
    # 1. Detecção de informações pessoais
    force_learn = st.session_state.learning_system.should_force_learn(user_input)
    
    # 2. Decisão inteligente: Sempre aprende se for informação pessoal!
    if force_learn:
        print(f"[Memória]: Informação pessoal detectada! Aprendizado forçado.")
        run_learning_step(
            context=st.session_state.messages[-5:],
            user_input=user_input,
            assistant_response=response,
            force_learn=True
        )
    elif random.random() < 0.1:  # Apenas 10% para outras informações
        print(f"[Memória]: Aprendizado aleatório ativado (10% chance).")
        run_learning_step(
            context=st.session_state.messages[-5:],
            user_input=user_input,
            assistant_response=response,
            force_learn=False
        )
# INTERFACE PRINCIPAL STREAMLIT (Design de Chat)
# ========================================================================

def main():
    """Função principal da aplicação Streamlit."""
    
    initialize_session_state()

    # Colunas: Status (30%) | Chat (70%)
    status_col, chat_col = st.columns([0.30, 0.70])

    # --- Coluna de Status (Esquerda - Painel Otimizado) ---
    with status_col:
        st.header("✨ Status LayLay")
        
        # 1. Emoção em tempo real (Painel principal)
        mood = st.session_state.personality.get_current_mood()
        st.info(f"**Atual:** {mood.capitalize()}")
        
        st.markdown("---")
        
        # 2. Informações do Usuário (Painel de Memória Simples)
        # 2. Informações do Usuário (Painel Completo)
        st.subheader("👤 Perfil do Usuário")
        user_facts_dict = st.session_state.learning_system.get_user_data()
        
        # Organiza as informações em categorias
        with st.expander("📋 Ver Perfil Completo", expanded=True):
            
            # Nome (sempre mostra)
            user_name = user_facts_dict.get("nome_usuario", "Anônimo")
            st.markdown(f"**📝 Nome:** {user_name}")
            
            # Idade
            if "idade" in user_facts_dict:
                st.markdown(f"**🎂 Idade:** {user_facts_dict['idade']} anos")
            
            # Gostos e Interesses
            gostos = []
            interesses = []
            
            for key, value in user_facts_dict.items():
                if key != "nome_usuario" and key != "idade":
                    if "gosto" in key or "gosta" in key:
                        gostos.append(f"{key.replace('gosto_', '').replace('_', ' ')}: {value}")
                    elif "interesse" in key:
                        interesses.append(f"{key.replace('interesse_', '').replace('_', ' ')}: {value}")
                    else:
                        interesses.append(f"{key.replace('_', ' ')}: {value}")
            
            if gostos:
                st.markdown("**💕 Gostos:**")
                for gosto in gostos:
                    st.markdown(f"  • {gosto}")
            
            if interesses:
                st.markdown("**🎯 Outros Interesses:**")
                for interesse in interesses:
                    st.markdown(f"  • {interesse}")
            
            if not gostos and not interesses and "idade" not in user_facts_dict:
                st.markdown("*🤷‍♂️ Ainda não conheço muito sobre você...*")
                st.markdown("*Diga algo como: 'Gosto de mangá', 'Tenho 25 anos', etc.*")
        
        # 3. Memória Detalhada
        st.markdown("---")
        st.subheader("🧠 Memória de Longo Prazo")
        all_facts_string = st.session_state.learning_system.get_all_facts_as_string()
        
        with st.expander("Ver fatos aprendidos (Para a IA)"):
            st.code(all_facts_string, language="text") 
            
        # 4. Opções de Controle
        st.markdown("---")
        if st.button("🔄 Reiniciar e Limpar", use_container_width=True, type="primary"):
            st.session_state.messages = [
                {"role": "assistant", "content": "Oi 💕 Eu sou a LayLay! Como você tá hoje?"}
            ]
            st.session_state.memory.context.clear()
            st.rerun()

    # --- Coluna de Chat (Direita - Foco Principal) ---
    with chat_col:
        st.header("💬 Conversa")
        # Altura grande para o chat parecer um aplicativo fixo
        chat_container = st.container(height=800) 
        
        with chat_container:
            # 🌟 OTIMIZAÇÃO: Garante que TODAS as mensagens (incluindo a primeira) 
            # sejam renderizadas dentro do chat_container e com o st.chat_message.
            for message in st.session_state.messages:
                # Avatares coloridos para clareza
                avatar = "💖" if message["role"] == "assistant" else "👤"
                with st.chat_message(message["role"], avatar=avatar):
                    st.markdown(message["content"])

    # --- Campo de entrada (Sempre na parte inferior) ---
    user_input = st.chat_input("Escreva algo para a LayLay...")
    
    if user_input:
        handle_user_input(user_input)
        st.rerun()

# ========================================================================
# EXECUÇÃO
# ========================================================================

if __name__ == "__main__":
    main()