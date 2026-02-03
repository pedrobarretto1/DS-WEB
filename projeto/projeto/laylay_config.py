# laylay_config.py

from typing import List, Dict

# ============================================================================
# CONFIGURAÇÕES GLOBAIS
# ============================================================================

class Config:
    """Centraliza todas as configurações."""
    
    # Configurações do Banco de Dados
    DB_NAME = "laylay_final_memory.db"
    DB_TIMEOUT = 10.0
    
    # Configurações de Memória e Contexto
    MAX_CONTEXT = 15
    CACHE_SIZE = 100
    
    # Configurações de Personalidade e Emoção
    SENTIMENT_THRESHOLD = 0.5
    EMOTION_DECAY_RATE = 0.95
    EMOTION_UPDATE_FACTOR = 0.2
    
    # Configurações de Resposta
    RESPONSE_TIMEOUT = 5.0
    
    # Configurações de Personalidade (Traits)
    PERSONALITY_TRAITS: Dict[str, float] = {
        "racionalidade": 0.85,
        "emotividade": 0.95,
        "amizade": 1.0,
        "empatia": 0.98,
        "humor": 0.75,
        "curiosidade": 0.90 # Adicionado para corrigir KeyError
    }

# ============================================================================
# DADOS PARA NLG (VOCABULÁRIO)
# ============================================================================

class NLGData:
    """Dados estáticos para o Gerador de Linguagem Natural (NLG)."""
    
    VOCABULARIO: Dict[str, List[str]] = {
        "saudacao": ["Olá", "Oi", "E aí", "Bem-vindo", "Prazer em conversar", "Tudo bem?", "Como vai?", "Que bom te ver", "Diga lá", "Fala, meu amigo(a)"],
        "confirmacao": ["Entendi", "Claro", "Sim", "Com certeza", "Exatamente", "Perfeito", "Concordo", "Isso mesmo", "Faz sentido", "Correto", "Sem dúvida"],
        "negacao": ["Não", "De jeito nenhum", "Discordo", "Não acho"],
        "gratidao": ["Obrigada", "Muito obrigada", "Agradeço", "Valeu"],
        "desculpa": ["Desculpe", "Peço desculpas", "Sinto muito", "Lamento"],
        "curiosidade": ["Que interessante", "Fascinante", "Intrigante", "Curioso"],
        "entusiasmo": ["Que legal", "Incrível", "Fantástico", "Maravilhoso"],
        "reflexao": ["Deixe-me pensar", "Hmm", "Interessante ponto", "Que bom questionar", "É uma boa pergunta", "Vou refletir sobre isso", "Isso me faz pensar", "Que complexo", "Preciso processar isso"],
        "empatia": ["Entendo como você se sente", "Compreendo", "Sinto sua emoção", "Estou aqui para você", "Que pena", "Que bom que está compartilhando", "Me preocupo com você"],
        "encerramento": ["Até logo", "Tchau", "Volte sempre", "Foi um prazer conversar", "Fique bem", "A gente se fala", "Um abraço virtual"],
        "girias": ["Massa", "Top", "Show", "Mano", "Tipo assim", "Na moral", "Demais", "Que brisa"]}
    
    ESTRUTURAS_FRASE: List[str] = [
        "{saudacao}! {reflexao} sobre o que você disse.",
        "{confirmacao}. {adjetivo} observação! {verbo} mais sobre isso.",
        "{curiosidade}! Eu {verbo} que {substantivo} é {adjetivo}.",
        "{empatia}. Você {verbo} {adjetivo} com isso.",
        "{entusiasmo}! Eu {verbo} {adjetivo} com isso.",
        "Eu {verbo} que {substantivo} {verbo} {adjetivo}. {reflexao}.",
        "O {substantivo} que você {verbo} é {adjetivo}. {curiosidade}?",
        "Sua {ideia} sobre {substantivo} é {adjetivo}. {confirmacao}.",
        "Eu {verbo} que {substantivo} é {adjetivo}, {conectores} isso me {verbo} a {reflexao}.",
        "{girias}! {confirmacao}, {substantivo} é {adjetivo}."
        "{reflexao}... Você {verbo} que {substantivo} é {adjetivo}?",
        "{confirmacao}! {adjetivo} ponto. Me conte mais sobre {substantivo}.",
        "{empatia}. Você {verbo} {adjetivo} sobre isso.",
        "{entusiasmo} Você {verbo} {adjetivo} com {substantivo}!"
    ]
    
    CONECTORES: List[str] = [
        "Além disso,", "Por outro lado,", "Portanto,", "Assim,", "No entanto,",
        "Consequentemente,", "Igualmente,", "De fato,", "Aliás,", "Em outras palavras,"
    ]
    
    ADJETIVOS: List[str] = [
        "interessante", "fascinante", "incrível", "maravilhoso", "fantástico", "genial", "brilhante",  "curioso", "intrigante", "importante", "significativo", "relevante",
        "profundo", "complexo", "simples", "elegante", "belo", "único",
        "especial", "extraordinário", "notável", "impressionante", "legal",
        "bacana", "show", "top", "massa", "dahora"
    ]
    
    VERBOS: List[str] = [
        "penso", "acho", "considero", "creio", "imagino", "vejo", "sinto", "parece",     "compreendo", "entendo", "percebo", "noto", "observo",
        "gosto", "adoro", "amo", "aproveito", "desfruto",
        "aprendo", "descubro", "encontro", "busco", "procuro",
        "questiono", "analiso", "avalio", "julgo", "diria"
    ]
    
    SUBSTANTIVOS: List[str] = [
        "ideia", "conceito", "pensamento", "perspectiva", "ponto de vista", "opinião", "assunto",     "conhecimento", "sabedoria", "inteligência", "criatividade", "inovação",
        "amizade", "confiança", "empatia", "compreensão", "apoio",
        "desafio", "oportunidade", "possibilidade", "futuro", "presente",
        "mundo", "vida", "experiência", "aprendizado", "crescimento"
    ]
    
    ESTRUTURAS_RACIOCINIO: List[str] = [
        "Baseando-me no que sei, {fato1} e {fato2}. Portanto, {conclusao}.",
        "Pensando sobre isso... {fato1} me leva a crer que {conclusao}.",
        "Analisando a situação: {fato1}, {fato2}. Logo, {conclusao}.",
        "Se considerarmos que {fato1} e {fato2}, então {conclusao}.",
        "Meu raciocínio é: {fato1} implica que {conclusao}."
    ]
    
    CONCLUSAO_BASE: List[str] = [
        "isso é {adjetivo}",
        "você tem um ponto {adjetivo}",
        "isso merece reflexão {adjetivo}",
        "é uma questão {adjetivo}",
        "isso me faz pensar de forma {adjetivo}"
    ]
    
    ESTRUTURAS_PERGUNTA: List[str] = [
        "O que você acha sobre {topico}?",
        "Como você se sente em relação a {topico}?",
        "Você já pensou em {topico}?",
        "Qual é sua opinião sobre {topico}?",
        "Me conte mais sobre {topico}.",
        "Por que você acha que {topico} é importante?",
        "Como {topico} afeta você?",
        "Você gostaria de explorar {topico} mais a fundo?"
    ]
