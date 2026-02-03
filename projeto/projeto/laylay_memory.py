# laylay_memory.py

# ==============================================================
# 🧠 LAYLAY MEMORY SYSTEM - MEMÓRIA DE CURTO PRAZO
# ==============================================================
# Esta classe é responsável APENAS por gerenciar o contexto imediato
# da conversa (o histórico de mensagens).
# A memória de longo prazo (fatos aprendidos e persistência no DB)
# foi delegada ao 'laylay_learning_system.py' para modularidade.
# ==============================================================

class Memory:
    """Gerencia a memória de curto prazo (histórico da conversa)."""
    
    def __init__(self):
        # Contexto de Curto Prazo (lista de dicionários: [{"role": "user", "content": "..."}])
        self.context = []

    # ==============================================================
    # 🔹 CURTO PRAZO (CONVERSA IMEDIATA)
    # ==============================================================
    def add_to_context(self, role: str, content: str):
        """Adiciona mensagens ao contexto de curto prazo.

        Args:
            role (str): O papel da mensagem ("user" ou "assistant").
            content (str): O conteúdo da mensagem.
        """
        content = content.strip()
        if content:
            self.context.append({"role": role, "content": content})
            
            # Otimização: Limitar o tamanho do contexto (Ex: últimas 20 mensagens = 10 turnos)
            # Isso impede que o prompt da LLM fique muito grande e caro.
            if len(self.context) > 20:
                self.context = self.context[-20:]

    def get_context(self) -> list:
        """Retorna o histórico de curto prazo completo."""
        return self.context

    def clear_context(self):
        """Limpa a memória de curto prazo (reinicia a conversa)."""
        self.context = []
        print("[Memória]: Contexto de curto prazo limpo.")

    # ==============================================================
    # 🔹 ATALHO (LEGACY)
    # ==============================================================
    
    # Mantém a variável 'context' como atalho para self.context para 
    # garantir que outras partes do código que usam 'memory.context' continuem funcionando.
    @property
    def context(self):
        return self._context
    
    @context.setter
    def context(self, value):
        self._context = value

    # Nota: Todos os métodos de DB e Longo Prazo foram removidos daqui.