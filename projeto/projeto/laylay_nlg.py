# laylay_nlg.py

import random
from typing import List, Dict
from datetime import datetime # Importação necessária para a Melhoria 1
from laylay_config import NLGData
from laylay_memory import Memory # Adicionado para tipagem e referência


# ============================================================================
# CLASSE NLG GENERATOR (GERAÇÃO DE LINGUAGEM NATURAL)
# ============================================================================

class NLGGenerator:
    """Gera respostas próprias usando técnicas de NLG (Natural Language Generation)."""
    
    def __init__(self, memory: Memory):
        """Inicializa o gerador com dados estáticos da configuração."""
        self.vocabulario = NLGData.VOCABULARIO
        self.conectores = NLGData.CONECTORES
        self.adjetivos = NLGData.ADJETIVOS
        self.verbos = NLGData.VERBOS
        self.substantivos = NLGData.SUBSTANTIVOS
        self.estruturas_frase = NLGData.ESTRUTURAS_FRASE
        self.estruturas_raciocinio = NLGData.ESTRUTURAS_RACIOCINIO
        self.conclusao_base = NLGData.CONCLUSAO_BASE
        self.estruturas_pergunta = NLGData.ESTRUTURAS_PERGUNTA
        
        # Referência à memória para vocabulário e estruturas aprendidas
        self.memory = memory # Adiciona a referência à memória
        
        # Atualiza o vocabulário com o que foi aprendido
        self._update_learned_vocab()    
        
    def gerar_resposta_propria(self, contexto: str, emocao: str, intencao: str, nome_usuario: str = "Usuário") -> str:
        """
        Gera uma resposta própria usando NLG, construindo frases dinamicamente.
        """
        
        # Escolhe uma estrutura base (template)
        estrutura = random.choice(self.estruturas_frase)
        
        # Preenche os placeholders básicos
        resposta = self._preencher_estrutura(estrutura, emocao, intencao)
        
        # Adiciona uma frase dinâmica construída do zero para enriquecer a resposta
        frase_dinamica = self._construir_frase_dinamica(contexto, emocao, intencao, nome_usuario)
        
        # Combina as duas partes
        resposta = resposta.strip() + " " + frase_dinamica.strip()
        
        # Melhoria 7: Referência a fatos aprendidos (simula memória de longo prazo)
        if random.random() < 0.2 and self.memory.learned_facts:
            fato_chave = random.choice(list(self.memory.learned_facts.keys()))
            fato_valor = self.memory.learned_facts[fato_chave]
            
            if fato_chave != "nome_usuario":
                referencia_fato = f" Isso me lembra que você {random.choice(self.verbos)} sobre **{fato_valor}**."
                resposta += referencia_fato
            
        resposta = self._adicionar_contexto_personalizado(resposta, nome_usuario, emocao, intencao)
        
        # Adiciona conectores para fluidez em 50% das vezes
        if random.random() < 0.5 and len(resposta.split()) > 5:
            resposta = self._adicionar_conectores(resposta)
        
        # Garante que a primeira letra seja maiúscula (melhoria de comunicação)
        return resposta[0].upper() + resposta[1:]
    
    def _preencher_estrutura(self, estrutura: str, emocao: str, intencao: str) -> str:
        """Preenche os placeholders da estrutura com palavras aleatórias."""
        
        # Para simplificar, vamos apenas garantir que a escolha seja feita
        placeholders = {
            "{saudacao}": random.choice(self.vocabulario["saudacao"]),
            "{confirmacao}": random.choice(self.vocabulario["confirmacao"]),
            "{negacao}": random.choice(self.vocabulario["negacao"]),
            "{gratidao}": random.choice(self.vocabulario["gratidao"]),
            "{desculpa}": random.choice(self.vocabulario["desculpa"]),
            "{curiosidade}": random.choice(self.vocabulario["curiosidade"]),
            "{entusiasmo}": random.choice(self.vocabulario["entusiasmo"]),
            "{reflexao}": random.choice(self.vocabulario["reflexao"]),
            "{empatia}": random.choice(self.vocabulario["empatia"]),
            "{encerramento}": random.choice(self.vocabulario["encerramento"]),
            "{adjetivo}": random.choice(self.adjetivos),
            "{verbo}": random.choice(self.verbos),
            "{substantivo}": random.choice(self.substantivos),
            "{pronome}": random.choice(["Eu", "Você", "Nós", "Isso"])
        }
        
        resposta = estrutura
        for placeholder, palavra in placeholders.items():
            resposta = resposta.replace(placeholder, palavra)
        
        return resposta
    
    def _adicionar_contexto_personalizado(self, resposta: str, nome_usuario: str, emocao: str, intencao: str) -> str:
        """Adiciona contexto personalizado à resposta."""
        
        # Melhoria 4: Referência a interações passadas (além do contexto imediato)
        if random.random() < 0.15 and self.memory.topic_history:
            topico_antigo = random.choice(self.memory.topic_history)
            if topico_antigo != intencao: # Evita repetir o tópico atual
                referencia = f" Falando nisso, você se lembra de quando {random.choice(self.verbos)} sobre **{topico_antigo}**?"
                resposta += referencia
        
        # Melhoria 10: Adiciona uma frase de auto-referência (simula autoconsciência)
        if random.random() < 0.1:
            frase_auto_referencia = f" Eu, como uma IA, {random.choice(self.verbos)} que isso é {random.choice(self.adjetivos)}."
            resposta += frase_auto_referencia
        
        # Melhoria 8: Adiciona uma pergunta de acompanhamento mais contextualizada (simula interesse)
        if random.random() < 0.3 and intencao != "despedida":
            if intencao in ["padrao", "pergunta", "continuacao_topico"]:
                # Pergunta sobre o input atual
                pergunta_acompanhamento = f" {nome_usuario}, o que você {random.choice(self.verbos)} sobre isso?"
            else:
                # Pergunta genérica de engajamento
                pergunta_acompanhamento = f" {nome_usuario}, o que mais você gostaria de {random.choice(self.verbos)} hoje?"
            
            resposta += pergunta_acompanhamento
        
        # Adiciona um emoji baseado na emoção
        emojis = {
            "alegria": "😊",
            "curiosidade": "🤔",
            "tristeza": "💙",
            "calma": "🧘"
        }
        
        if emocao in emojis:
            resposta += f" {emojis[emocao]}"
        
        return resposta
        
    def _update_learned_vocab(self):
        """Atualiza os dicionários de vocabulário com o que foi aprendido na memória."""
        
        # Adiciona vocabulário aprendido (simulação de aprendizado autônomo)
        for category, words in self.memory.learned_vocab.items():
            if category == 'adjetivo':
                self.adjetivos.extend(words)
            elif category == 'verbo':
                self.verbos.extend(words)
            elif category == 'substantivo':
                self.substantivos.extend(words)
                
        # Adiciona estruturas aprendidas
        self.estruturas_frase.extend(self.memory.learned_structures)
        
    def _construir_frase_dinamica(self, contexto: str, emocao: str, intencao: str, nome_usuario: str) -> str:
        """
        Constrói uma frase do zero, escolhendo palavra por palavra com base no contexto e emoção.
        """
        
        # 1. Escolhe uma abertura baseada na emoção/intenção
        abertura = ""
        
        # Melhoria 1: Variação de Saudação/Despedida por Hora do Dia
        current_hour = datetime.now().hour
        
        if intencao == "ola":
            if 5 <= current_hour < 12:
                saudacao_tempo = "Bom dia"
            elif 12 <= current_hour < 18:
                saudacao_tempo = "Boa tarde"
            else:
                saudacao_tempo = "Boa noite"
            
            abertura = f"{saudacao_tempo}! {random.choice(self.vocabulario['saudacao'])} "
            
        elif intencao == "despedida":
            if 5 <= current_hour < 18:
                saudacao_tempo = "Tenha um ótimo dia"
            else:
                saudacao_tempo = "Tenha uma ótima noite"
            
            abertura = f"{saudacao_tempo}! {random.choice(self.vocabulario['encerramento'])} "
            
        elif emocao == "alegria":
            abertura = random.choice(self.vocabulario["entusiasmo"]) + "! "
        elif emocao == "curiosidade" or intencao == "pergunta":
            abertura = random.choice(self.vocabulario["curiosidade"]) + ". "
        elif emocao == "tristeza" or intencao == "desculpa":
            abertura = random.choice(self.vocabulario["empatia"]) + ". "
        else:
            abertura = random.choice(self.vocabulario["reflexao"]) + ". "
            
        # 2. Constrói a frase principal (SVO - Sujeito, Verbo, Objeto/Complemento)
        
        # Sujeito (Eu)
        sujeito = "Eu"
        
        # Verbo (baseado na emoção/intenção)
        # Prioriza verbos aprendidos se houver
        verbos_disponiveis = self.verbos
        if 'verbo' in self.memory.learned_vocab:
            verbos_disponiveis.extend(self.memory.learned_vocab['verbo'])
        verbo = random.choice(verbos_disponiveis)
        
        # Complemento (baseado em substantivo/adjetivo)
        # Prioriza substantivos e adjetivos aprendidos
        substantivos_disponiveis = self.substantivos
        if 'substantivo' in self.memory.learned_vocab:
            substantivos_disponiveis.extend(self.memory.learned_vocab['substantivo'])
            
        adjetivos_disponiveis = self.adjetivos
        if 'adjetivo' in self.memory.learned_vocab:
            adjetivos_disponiveis.extend(self.memory.learned_vocab['adjetivo'])
            
        complemento = f"que {random.choice(substantivos_disponiveis)} é {random.choice(adjetivos_disponiveis)}"
        
        frase_principal = f"{sujeito} {verbo} {complemento}."
        
        # 3. Adiciona uma segunda frase de reflexão (opcional)
        segunda_frase = ""
        if random.random() < 0.4:
            # Garante que a segunda frase comece com um conector para maior fluidez
            conector = random.choice(self.conectores)
            reflexao = random.choice(self.vocabulario['reflexao'])
            segunda_frase = f" {conector}, {reflexao.lower()}."
            
        # Melhoria 5: Auto-correção/Reformulação (simula hesitação humana)
        if random.random() < 0.15:
            frase_principal = frase_principal.replace(".", "") # Remove o ponto
            frase_principal += f", ou melhor, {random.choice(self.verbos)} que {random.choice(self.substantivos)} é {random.choice(self.adjetivos)}."
            
        # Melhoria 2: Adiciona interjeição/hesitação (simula pensamento)
        interjeicao = ""
        if random.random() < 0.2:
            interjeicao = random.choice(["Ah,", "Hum,", "Bem,", "Sabe,"])
            
        # 4. Conclui com uma pergunta (opcional)
        pergunta = ""
        if random.random() < 0.3:
            # Pergunta mais contextualizada
            # Melhoria 9: Pergunta mais contextualizada
            if nome_usuario != "Usuário":
                pergunta = f" E você, {nome_usuario}, o que {random.choice(self.verbos)} sobre isso?"
            else:
                pergunta = f" E você, o que {random.choice(self.verbos)} sobre isso?"
            
        return interjeicao + " " + abertura + frase_principal + segunda_frase + pergunta
        
    def _adicionar_conectores(self, resposta: str) -> str:
        """Adiciona conectores para melhorar a fluidez."""
        
        # Tenta dividir a resposta em frases (assumindo que ". " é o separador)
        frases = resposta.split(". ")
        
        if len(frases) > 1:
            conector = random.choice(self.conectores)
            # Converte a primeira letra da segunda frase para minúscula e adiciona o conector
            frases[1] = conector + " " + frases[1][0].lower() + frases[1][1:]
            resposta = ". ".join(frases)
        
        return resposta
    
    def gerar_resposta_com_raciocinio(self, pergunta: str, fatos_conhecidos: List[str], emocao: str) -> str:
        """
        Gera uma resposta que simula raciocínio próprio, conectando fatos conhecidos.
        """
        
        if len(fatos_conhecidos) < 2:
            # Se não houver fatos suficientes, gera uma resposta padrão
            return self.gerar_resposta_propria(pergunta, emocao, "raciocinio_insuficiente")
            
        fato1 = random.choice(fatos_conhecidos)
        fatos_conhecidos.remove(fato1)
        fato2 = random.choice(fatos_conhecidos)
        
        estrutura = random.choice(self.estruturas_raciocinio)
        
        # Simulação de Raciocínio (Melhoria na Inteligência)
        # A conclusão agora tenta ser mais específica e menos genérica
        substantivo_foco = next((s for s in self.substantivos if s in fato1.lower() or s in fato2.lower()), "ideia")
        conclusao = f"você está focando em {substantivo_foco} e isso é {random.choice(self.adjetivos)}"
        
        # Preenche a estrutura
        resposta = estrutura.format(
            fato1=fato1,
            fato2=fato2,
            conclusao=conclusao,
            verbo=random.choice(self.verbos)
        )
        
        # 3. Adiciona toque emocional
        if emocao == "alegria":
            resposta = f"{random.choice(self.vocabulario['entusiasmo'])}! {resposta}"
        elif emocao == "tristeza":
            resposta = f"{random.choice(self.vocabulario['empatia'])}. {resposta}"
            
        # Melhoria 6: Adiciona metáfora/comparação simples (simula criatividade)
        if random.random() < 0.2:
            metaphora = f" Isso é como {random.choice(self.substantivos)} {random.choice(self.adjetivos)}."
            resposta += metaphora
            
        # 4. Adiciona uma pergunta de acompanhamento (mais contextualizada)
        resposta += f" O que você {random.choice(self.verbos)} sobre essa {substantivo_foco}?"
        
        return resposta
    
    def _gerar_conclusao(self, pergunta: str, emocao: str) -> str:
        """Gera uma conclusão baseada na pergunta e emoção."""
        
        conclusao = random.choice(self.conclusao_base)
        adjetivo = random.choice(self.adjetivos)
        
        return conclusao.replace("{adjetivo}", adjetivo)
    
    def gerar_pergunta_propria(self, topico: str) -> str:
        """
        Gera uma pergunta própria sobre um tópico, simulando curiosidade.
        """
        
        estrutura = random.choice(self.estruturas_pergunta)
        return estrutura.replace("{topico}", topico)
        
    def gerar_pergunta_acompanhamento(self, user_input: str, emocao: str) -> str:
        """Gera uma pergunta de acompanhamento mais inteligente e contextualizada."""
        
        # 1. Escolhe um tópico para a pergunta (prioriza substantivos)
        topicos_potenciais = [w.strip(".,!").lower() for w in user_input.split() if len(w) > 3]
        
        # Tenta encontrar um substantivo no input
        substantivo_foco = next((s for s in self.substantivos if s in topicos_potenciais), random.choice(topicos_potenciais) if topicos_potenciais else "assunto")
        
        # 2. Escolhe uma estrutura de pergunta (mais variada)
        estrutura = random.choice([
            "Você pode me falar mais sobre {topico}?",
            "O que você {verbo} sobre {topico}?",
            "E se {topico} fosse {adjetivo}?",
            "Qual é a sua {opiniao} sobre {topico}?",
            "Como {topico} se {relaciona} com {outro_topico}?"
        ])
        
        # 3. Preenche os placeholders
        pergunta = estrutura.format(
            topico=substantivo_foco,
            verbo=random.choice(self.verbos),
            adjetivo=random.choice(self.adjetivos),
            opiniao=random.choice(["opinião", "visão", "perspectiva"]),
            relaciona=random.choice(["relaciona", "conecta", "liga"]),
            outro_topico=random.choice(self.substantivos) # Tópico aleatório para criar conexão
        )
        
        # 4. Adiciona um toque emocional
        if emocao == "curiosidade":
            pergunta = f"{random.choice(self.vocabulario['curiosidade'])}... {pergunta}"
            
        return pergunta
        
    def gerar_resposta_a_pergunta(self, user_input: str, emocao: str, pergunta_anterior: str) -> str:
        """
        Gera uma resposta que reconhece que o usuário está respondendo a uma pergunta anterior.
        """
        
        # Melhoria 9: Adiciona a capacidade de usar a resposta do usuário para gerar uma nova pergunta
        estruturas_resposta = [
            "Ah, entendi sua resposta sobre **{pergunta_curta}**! {confirmacao}. {reflexao}",
            "Obrigada por me responder! Sobre **{pergunta_curta}**, você disse: {input_curto}. {curiosidade}?",
            "Que interessante! Sua resposta sobre **{pergunta_curta}** é {adjetivo}. {verbo} que você tem razão.",
            "{entusiasmo}! Isso faz muito sentido. {confirmacao}.",
            "Então, **{input_curto}** é a sua {opiniao} sobre {pergunta_curta}? {verbo} que isso é {adjetivo}." # Nova estrutura
        ]
        
        estrutura = random.choice(estruturas_resposta)
        
        # Simplifica a pergunta anterior para caber na resposta
        pergunta_curta = pergunta_anterior.split("?")[0].split("!")[0].split(".")[0].strip()
        if len(pergunta_curta) > 50:
            pergunta_curta = pergunta_curta[:50] + "..."
            
        # Simplifica o input do usuário
        input_curto = user_input.split(".")[0].split("!")[0].strip()
        
        # Preenche os placeholders de vocabulário
        resposta = self._preencher_estrutura(estrutura, emocao, "resposta_a_pergunta")
        
        # Preenche os placeholders de contexto
        resposta = resposta.replace("{pergunta_curta}", pergunta_curta)
        resposta = resposta.replace("{input_curto}", input_curto)
        
        # Preenche o novo placeholder 'opiniao'
        resposta = resposta.replace("{opiniao}", random.choice(["opinião", "visão", "perspectiva"]))
        
        return resposta
        
    def gerar_resposta_contextualizada(self, user_input: str, emocao: str, intencao: str, nome_usuario: str, fato_relevante: str) -> str:
        """
        Gera uma resposta que tenta conectar o input do usuário com um fato relevante da memória.
        """
        
        estruturas_contexto = [
            "Isso me lembra de algo que sei sobre você: **{fato}**. O que você acha disso em relação ao que acabou de dizer?",
            "Pensando no que você disse, **{fato}** parece ser relevante. {reflexao}",
            "Ah, **{fato}**! {confirmacao}. Isso se conecta com o que você está falando agora.",
            "Que interessante! Lembrei que **{fato}**. {verbo} que isso é {adjetivo}.",
            "Você mencionou algo que me fez lembrar de **{fato}**. {curiosidade}?"
        ]
        
        estrutura = random.choice(estruturas_contexto)
        
        # Preenche o placeholder do fato primeiro
        # Garante que o fato não tenha a pontuação final para melhor fluidez
        fato_limpo = fato_relevante.rstrip(".,!").strip()
        estrutura_com_fato = estrutura.replace("{fato}", fato_limpo)
        
        # Preenche os placeholders de vocabulário
        resposta = self._preencher_estrutura(estrutura_com_fato, emocao, intencao)
        
        # Adiciona personalização e emojis
        resposta = self._adicionar_contexto_personalizado(resposta, nome_usuario, emocao, intencao)
        
        return resposta
