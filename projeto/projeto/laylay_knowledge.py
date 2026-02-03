import requests

class KnowledgeModule:
    def search(self, query: str):
        """Faz uma busca simples no DuckDuckGo API."""
        try:
            response = requests.get("https://api.duckduckgo.com/", params={
                "q": query, "format": "json", "no_html": 1
            })
            data = response.json()
            if data.get("AbstractText"):
                return data["AbstractText"]
            elif data.get("RelatedTopics"):
                return data["RelatedTopics"][0].get("Text", "Não encontrei nada exato 😅")
            else:
                return "Hmm... não achei nada sobre isso 💭"
        except Exception as e:
            return f"Erro ao pesquisar: {e}"
