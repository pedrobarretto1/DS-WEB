'''
Este módulo contém a classe para interagir com a API da OpenRouter.
Foi otimizado com mecanismos de retry e tratamento de erro robusto.
'''
import os
import time
from openai import OpenAI, RateLimitError, APIError
from typing import List, Dict

class OpenRouterLLM:
    """
    Classe para interagir com a API da OpenRouter usando a biblioteca OpenAI.
    """
    
    # Configurações de Retry
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # Segundos de espera inicial

    # Padrão: Modelo Mistral 7B (Mais estável em tiers gratuitos/baixo custo)
    def __init__(self, model: str = "mistralai/mistral-7b-instruct"):
        self.model = model
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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"
        )

    def generate_response(self, system_prompt: str, messages: List[Dict[str, str]]) -> str:
        """
        Gera uma resposta da LLM com mecanismo de retry e tratamento de erro robusto.
        Sempre retorna uma string para evitar o erro 'NoneType'.
        """
        full_messages = [{"role": "system", "content": system_prompt}] + messages
        
        for attempt in range(self.MAX_RETRIES):
            try:
                # 1. Tenta a chamada à API
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=full_messages,
                    temperature=0.75,
                    max_tokens=400,
                    timeout=30.0 # Timeout para evitar travamentos longos de rede
                )
                
                # 2. Verificação robusta do conteúdo (Previne 'NoneType' errors)
                if response and response.choices and response.choices[0].message and response.choices[0].message.content:
                    return response.choices[0].message.content.strip()
                else:
                    # Resposta inesperada (vazia ou incompleta) sem erro de exceção
                    print(f"[ERRO LLM]: Resposta inesperada/vazia da API na tentativa {attempt + 1}. Tentando novamente...")
                    if attempt < self.MAX_RETRIES - 1:
                        time.sleep(self.RETRY_DELAY)
                        continue
                    else:
                        break # Sai se for a última tentativa

            except RateLimitError as e:
                # 3. Erro de Rate Limit (Não deve tentar novamente, é um limite rígido)
                print(f"[ERRO LLM]: Rate Limit Excedido. {e}")
                return f"⚠️ Ops! Limite de uso excedido ({self.model}). Por favor, espere um pouco ou tente um modelo diferente. (Detalhes: {e})"
            
            except (APIError, Exception) as e:
                # 4. Trata erros transientes de API ou rede, e tenta novamente
                print(f"[ERRO LLM]: Erro de conexão/API na tentativa {attempt + 1}: {e}. Tentando novamente...")
                if attempt < self.MAX_RETRIES - 1:
                    # Delay exponencial: 2s, 4s, 8s...
                    time.sleep(self.RETRY_DELAY * (attempt + 1)) 
                    continue
                else:
                    # 5. Falha final após todas as tentativas
                    print(f"[ERRO LLM]: Falha após {self.MAX_RETRIES} tentativas.")
                    return f"⚠️ Ops! Ocorreu uma falha de comunicação persistente com a LayLay. Por favor, verifique sua conexão ou tente mais tarde. (Detalhes: {e})"
        
        # Fallback final se o loop terminar sem um retorno bem-sucedido
        return "Ops! Parece que minha conexão falhou após várias tentativas. Pode tentar de novo? 😅"