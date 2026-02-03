from datetime import datetime

nome = input("qual o seu nome? ")
print(f"bem-vindo, {nome}!")

def tarefa_ja_existe(nome_nova_tarefa):
    linhas = ler_tarefas()
    for i in range(0, len(linhas), 5):
        #o strip remover os espaços 
        #o replace remove oq não faz parte da tarefa como isso linhas[i].replace("vc tem que ", "") oq vem depois é oq não faz parte que é o ("vc tem que ", "")
        tarefa_salva = linhas[i].replace("vc tem que ", "").strip()
        if tarefa_salva.lower() == nome_nova_tarefa.lower():
            return True
    return False

def criar_tarefa():
    tarefa = input("qual a tarefa? ")

    if tarefa_ja_existe(tarefa):
        print(f" A tarefa '{tarefa}' já existe na tua lista!")
        return

    prioridade = int(input("prioridade (1-Alta, 2-Média, 3-Baixa): "))
    if prioridade == 1:
        prioridade_texto = "Alta"
    elif prioridade == 2:
        prioridade_texto = "Média"
    elif prioridade == 3:
        prioridade_texto = "Baixa"
    else:
        prioridade_texto = "Inválida"

    status = int(input("status (1-em andamento, 2-finalizada): "))
    if status == 1:
        status_texto = "em andamento"
    elif status == 2:
        status_texto = "finalizada"
    else:
        status_texto = "inválido"
# o .now() captura oatual no contexto com datetime captura o momento atual
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M")

    with open("tarefa.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"vc tem que {tarefa}\n")
        arquivo.write(f"com prioridade nivel {prioridade_texto}\n")
        arquivo.write(f"os status dele é {status_texto}\n\n")
        arquivo.write(f"criada em: {data_formatada}\n\n")
        arquivo.write("concluída em: --\n\n")

    print(" tarefa salva com sucesso!")

def ler_tarefas():
    #o try e o except é como o if e else mas serve pra evita que o programa trave com respostas inesperadas
    try:
        with open("tarefa.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        return []

    linhas_limpas = []
    for linha in linhas:
        if linha.strip():
            linhas_limpas.append(linha.strip())

    return linhas_limpas

def mostrar_tarefas():
    linhas = ler_tarefas()

    if not linhas:
        print("nenhuma tarefa cadastrada.")
        return

    numero = 1
# Se mudar para 4 linhas, o passo é 4. Se mudar para 5, o passo é 5.
    passo = 5

    for i in range(0, len(linhas), passo):
# Só tenta ]mostra ao usuario se o índice i + (passo-1) existir na lista
        if i + (passo - 1) < len(linhas):
            print(f" tarefa de {nome} - {numero} - {linhas[i]} - {linhas[i+3]}")
            numero += 1
        else:
            print("")

def apagar_tarefa():
    linhas = ler_tarefas()
    if not linhas:
        print("não há tarefas para apagar.")
        return

    mostrar_tarefas()
    try:
        escolha = int(input("qual tarefa deseja apagar? "))
        
        # aqui define o numero de linhas que cada tarefa tem
        n_linhas = 5 
        
        inicio = (escolha - 1) * n_linhas
        
        # Verifica se o índice existe antes de apagar
        if 0 <= inicio < len(linhas):
            del linhas[inicio : inicio + n_linhas]
            
            with open("tarefa.txt", "w", encoding="utf-8") as arquivo:
                for i in range(0, len(linhas), n_linhas):
                    if i + (n_linhas - 1) < len(linhas):
                        for offset in range(n_linhas):
                            arquivo.write(linhas[i + offset] + "\n")
                        arquivo.write("\n")
            
            print("Tarefa apagada com sucesso!")
        else:
            print("Número de tarefa inválido.")
            
    except ValueError:
        print("Erro: Digite um número válido.")

def editar_tarefa():
    linhas = ler_tarefas()

    if not linhas:
        print("Não há tarefas para editar.")
        return

    mostrar_tarefas()
    escolha = int(input("Qual tarefa deseja editar? "))

    inicio = (escolha - 1) * 3
    novo_nome = input("qual o novo nome da tarefa? ")

    nova_prioridade = int(input("Nova prioridade (1-Alta, 2-Média, 3-Baixa): "))
    if nova_prioridade == 1: p_texto = "Alta"
    elif nova_prioridade == 2: p_texto = "Média"
    else: p_texto = "Baixa"

    novo_status = int(input("Novo status (1-em andamento, 2-finalizada): "))
    if novo_status == 1: s_texto = "em andamento"
    else: s_texto = "finalizada"

    linhas[inicio] = f"o nome da tarefa é {novo_nome}"
    linhas[inicio + 1] = f"com prioridade nivel {p_texto}"
    linhas[inicio + 2] = f"os status dele é {s_texto}"

    with open("tarefa.txt", "w", encoding="utf-8") as arquivo:
        for i in range(0, len(linhas), 5):
            arquivo.write(linhas[i] + "\n")
            arquivo.write(linhas[i+1] + "\n")
            arquivo.write(linhas[i+2] + "\n\n")
            arquivo.write(linhas[i+3] + "\n")
            arquivo.write(linhas[i+4] + "\n\n")

    print(" Tarefa editada com sucesso!")

def calcular_duracao(data_inicio_str, data_fim_str):
    formato = "%d/%m/%Y %H:%M"
    # o strptime Transformamos o texto em data transformando 03/01/2026 para %d/%m/%Y para o codigo intrepreta como uma data e não texto
    inicio = datetime.strptime(data_inicio_str, formato)
    fim = datetime.strptime(data_fim_str, formato)
    
    duracao = fim - inicio
    
    # Extrai dias, horas e minutos da diferença, apenas uma conta simples fazendo o tempo de diferença
    dias = duracao.days
    horas = duracao.seconds // 3600
    minutos = (duracao.seconds // 60) % 60
    
    return f"{dias} dias, {horas} horas e {minutos} minutos"

def finalizar_tarefa():
    linhas = ler_tarefas()
    if not linhas:
        print("Não há tarefas.")
        return

    mostrar_tarefas()
    escolha = int(input("Qual tarefa quer terminar? "))
    
    # i+0: tarefa, i+1: prioridade, i+2: status, i+3: data_criacao, i+4: data_conclusao
    inicio = (escolha - 1) * 5
    
    if "finalizada" in linhas[inicio + 2]:
        print("Esta tarefa já estava concluída!")
        return

    # Atualizar Status
    linhas[inicio + 2] = "os status dele é finalizada"
    
    # Registar Data de Conclusão
    # o strftime transforma a data ("%d/%m/%Y %H:%M") em uma str ("03/01/2026") é o oposto do strftime
    data_conclusao = datetime.now().strftime("%d/%m/%Y %H:%M")
    linhas[inicio + 4] = f"concluída em: {data_conclusao}"
    
    # 3. Calcular Duração
    data_criacao_limpa = linhas[inicio + 3].replace("criada em: ", "")
    tempo_gasto = calcular_duracao(data_criacao_limpa, data_conclusao)
    
    # Gravar de volta no ficheiro
    with open("tarefa.txt", "w", encoding="utf-8") as arquivo:
        for i in range(0, len(linhas), 5):
            arquivo.write(linhas[i] + "\n")
            arquivo.write(linhas[i+1] + "\n")
            arquivo.write(linhas[i+2] + "\n")
            arquivo.write(linhas[i+3] + "\n")
            arquivo.write(linhas[i+4] + "\n\n")

    print(f" Parabéns! Tarefa concluída.")
    print(f" voce levou {tempo_gasto} para terminar essa tarefa.")

    linha_prioridade = linhas[inicio + 1] 
    pontos_ganhos = 0
    if "Alta" in linha_prioridade:
        pontos_ganhos = 50
    elif "Média" in linha_prioridade:
        pontos_ganhos = 30
    else:
        pontos_ganhos = 10

    # Atualiza o total
    total_atual = carregar_pontos()
    novo_total = total_atual + pontos_ganhos
    salvar_pontos(novo_total)

    if (novo_total // 100) > ((novo_total - pontos_ganhos) // 100):
        print(" PARABENS VOCE SUBIU DE NÍVEL!")

    print(f" Parabéns! Você ganhou {pontos_ganhos} pontos, seu total é {novo_total}")

def carregar_pontos():
    try:
        with open("pontos.txt", "r") as arquivo:
            return int(arquivo.read())
    except (FileNotFoundError, ValueError):
        return 0  # Se o arquivo não existir, começa com 0

def salvar_pontos(total):
    with open("pontos.txt", "w") as arquivo:
        arquivo.write(str(total))

def carregar_xp():
    try:
        with open("perfil.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def salvar_xp(quantidade):
    total_atual = carregar_xp()
    novo_total = total_atual + quantidade
    with open("perfil.txt", "w") as f:
        f.write(str(novo_total))
    return novo_total

def exibir_status():
    xp_total = carregar_xp()
    nivel = (xp_total // 100) + 1
    xp_proximo_nivel = 100 - (xp_total % 100)
    titulo = obter_titulo(nivel)
    
    # Criando uma barra de progresso visual simples
    progresso = (xp_total % 100) // 10  # Cada 10 XP é um quadradinho
    barra = "■" * progresso + "□" * (10 - progresso)

    print("\n" + "="*30)
    print(f"      STATUS DE {nome.upper()}")
    print("="*30)
    print(f"Título: {titulo}")
    print(f"Nível:  {nivel}")
    print(f"XP:     [{barra}] {xp_total % 100}/100")
    print(f"Total:  {xp_total} XP acumulados")
    print(f"Falta:  {xp_proximo_nivel} XP para o próximo nível")
    print("="*30)

def obter_titulo(nivel):
    if nivel <= 5:
        return "🌱 Novato"
    elif nivel <= 10:
        return "⚔️ Executor"
    elif nivel <= 20:
        return "🛡️ Gerente de Projetos"
    elif nivel <= 50:
        return "🧙 Mestre da Produtividade"
    else:
        return "👑 Lenda Viva"
    
def limpar_tarefas_concluidas():
    linhas = ler_tarefas()
    if not linhas:
        print("A lista já está vazia.")
        return

    novas_linhas = []
    tarefas_removidas = 0
    
    # O passo depende de quantas linhas cada tarefa ocupa (estamos a usar 5)
    n_linhas = 5 

    for i in range(0, len(linhas), n_linhas):
        # Verificamos a linha do status (i+2)
        # Usamos o lower() para garantir que apanha "Finalizada" ou "finalizada"
        if "finalizada" not in linhas[i+2].lower():
            # Se NÃO está finalizada, guardamos na nova lista
            for offset in range(n_linhas):
                novas_linhas.append(linhas[i + offset])
        else:
            tarefas_removidas += 1

    if tarefas_removidas > 0:
        # Sobrescreve o ficheiro com a lista limpa
        with open("tarefa.txt", "w", encoding="utf-8") as arquivo:
            for i in range(0, len(novas_linhas), n_linhas):
                for offset in range(n_linhas):
                    arquivo.write(novas_linhas[i + offset] + "\n")
                arquivo.write("\n")
        
        print(f"🧹 Limpeza concluída! {tarefas_removidas} tarefas terminadas foram removidas.")
    else:
        print("✨ Não há tarefas finalizadas para limpar.")

while True:
    print("\n1 - criar tarefa")
    print("2 - ver tarefas")
    print("3 - apagar tarefa")
    print("4 - editar tarefa")
    print("5 - finalizar tarefa")
    print("6 - ver meu perfil")
    print("7 - limpar tarefas concluidas")
    print("8 - sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        criar_tarefa()
    elif opcao == "2":
        mostrar_tarefas()
    elif opcao == "3":
        apagar_tarefa()
    elif opcao == "4":     
        editar_tarefa()
    elif opcao == "5":     
        finalizar_tarefa()
    elif opcao == "6":     
        exibir_status()
    elif opcao == "7":
        limpar_tarefas_concluidas()
    elif opcao == "8":
        print("saindo...")
        break
    else:
        print("opção inválida")