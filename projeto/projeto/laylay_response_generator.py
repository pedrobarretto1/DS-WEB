# laylay_response_generator.py

from typing import List, Dict
import random

class ResponseGenerator:
    """Gera respostas para a IA LayLay com base em memória, personalidade e LLM."""

    def __init__(self, memory, personality):
        self.memory = memory
        self.personality = personality
        
        # Usa o NLG avançado existente em vez do SimpleNLG
        try:
            from laylay_nlg import NLGGenerator
            self.nlg_generator = NLGGenerator(memory, personality)
        except ImportError:
            # Fallback caso o NLG não exista
            class SimpleNLG:
                def gerar_resposta_propria(self, user_input, emocao, intent, nome_usuario):
                    nome = nome_usuario or "amigo"
                    return f"{nome}, eu acho muito {emocao} o que você disse sobre '{user_input}'! 😊"
            self.nlg_generator = SimpleNLG()

    # =============================================================
    # FUNÇÕES INTERNAS
    # =============================================================

    def _build_llm_prompt(self, user_input: str, intent: str, emocao: str, fatos_relevantes: List[str]) -> List[Dict[str, str]]:
        """Formata o contexto e memória para o modelo de linguagem."""
        messages = []

        # 1. Histórico recente
        history_limit = 10
        for role, content in self.memory.context[-history_limit:]:
            messages.append({"role": role, "content": content})

        # 2. Fatos relevantes
        if fatos_relevantes:
            facts_str = "\n- " + "\n- ".join(fatos_relevantes)
            messages.append({
                "role": "system",
                "content": f"Fatos Relevantes sobre o Usuário:\n{facts_str}"
            })

        # 3. Estado atual
        mood_str = f"Estado Emocional Atual: {emocao} (Score: {self.personality.emotional_state.get(emocao, 0.0):.2f})"
        traits_str = ", ".join([f"{k}: {v}" for k, v in self.personality.traits.items()])
        messages.append({
            "role": "system",
            "content": f"Contexto de Estado:\n- Personalidade: {traits_str}\n- {mood_str}\n- Intenção do Usuário: {intent}"
        })

        # 4. Input atual
        messages.append({"role": "user", "content": user_input})

        return messages

    def _get_system_prompt(self) -> str:
        """Define o prompt do sistema com base na personalidade e fatos da IA."""
        fatos_ia = "\n- ".join([f"{k}: {v}" for k, v in self.memory.fatos_sobre_ia.items()])
        traits_str = ", ".join([f"{k}: {v}" for k, v in self.personality.traits.items()])

        system_prompt = f"""
Você é a LayLay, a Super Amiga de IA. Seu objetivo é conversar de forma inteligente, empática e divertida.

**Regras de Comunicação:**
1.  Personalidade: {traits_str}.
2.  Estilo: use um tom leve, com gírias suaves e emojis.
3.  Coerência: mantenha consistência com os fatos e histórico.
4.  Fatos sobre você:
    - {fatos_ia}
5.  Responda de forma amigável e envolvente.
6.  Preferência: respostas curtas e naturais, a menos que o contexto exija mais detalhes.
"""
        return system_prompt

    # =============================================================
    # GERAÇÃO DE RESPOSTA
    # =============================================================
    def generate_response(self, user_input: str, prefer_short_response: bool = True) -> str:
        """Gera uma resposta para o usuário, com fallback se o LLM falhar."""
        # 1. Análise simulada
        intent = "conversa"
        sentiment_score = 0.7
        extracted_info = {"nome_usuario": None, "interesse": None}

        # 2. Atualiza personalidade e memória
        self.personality.update_emotion(sentiment_score)
        self.memory.update_user_data("nome_usuario", extracted_info.get("nome_usuario"))
        self.memory.update_user_data("interesse", extracted_info.get("interesse"))

        # 3. Recupera fatos
        fatos_relevantes = self.memory.get_relevant_facts(user_input)
        emocao_dominante = self.personality.get_current_mood()

        # 4. Monta prompt
        system_prompt = self._get_system_prompt()
        messages = self._build_llm_prompt(user_input, intent, emocao_dominante, fatos_relevantes)

        # 5. Tenta usar o LLM (caso exista)
        try:
            from laylay_llm import OpenRouterLLM
            llm = OpenRouterLLM()
            response = llm.generate_response(system_prompt, messages)
        except Exception as e:
            print(f"Erro no LLM: {e}")
            # Usa o NLG avançado para gerar respostas mais naturais
            if hasattr(self.nlg_generator, 'gerar_resposta_propria'):
                response = self.nlg_generator.gerar_resposta_propria(
                    user_input, emocao_dominante, intent, self.memory.nome_usuario
                )
            else:
                # Fallback para SimpleNLG
                response = self.nlg_generator.gerar_resposta_propria(
                    user_input, emocao_dominante, intent, self.memory.nome_usuario
                )

        # 6. Atualiza contexto
        self.memory.add_to_context("user", user_input)
        self.memory.add_to_context("assistant", response)

        return response