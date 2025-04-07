from model import add_categoria, add_despesa, get_categorias, get_despesas
from view import exibir_categorias, exibir_despesas, exibir_relatorio, mensagem, erro
from datetime import datetime

def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def cadastrar_categoria():
    nome = input("Nome da categoria: ")
    if not nome.strip():
        erro("Nome da categoria não pode ser vazio.")
        return
    categoria = add_categoria(nome)
    mensagem(f"Categoria '{categoria['nome']}' cadastrada com sucesso!")

def registrar_despesa():
    categorias = get_categorias()
    if not categorias:
        erro("Nenhuma categoria encontrada. Cadastre uma categoria primeiro.")
        return

    exibir_categorias(categorias)
    try:
        valor = float(input("Valor da despesa: R$ "))
        data_despesa = input("Data da despesa (DD-MM-YYYY): ")
        if not validar_data(data_despesa):
            erro("Data inválida! Use o formato DD-MM-YYYY.")
            return

        categoria_id = int(input("ID da categoria: "))
        if categoria_id not in [c["id"] for c in categorias]:
            erro("Categoria inexistente!")
            return

        descricao = input("Descrição da despesa: ")
        status = input("Status da despesa (Paga/Pendente): ").capitalize()
        if status not in ["Paga", "Pendente"]:
            erro("Status inválido. Use 'Paga' ou 'Pendente'.")
            return

    except ValueError:
        erro("Entrada inválida. Verifique os valores informados.")
        return

    despesa = add_despesa(valor, data_despesa, categoria_id, descricao, status)
    mensagem(f"Despesa registrada com sucesso!")

def consultar_despesas_por_periodo():
    inicio = input("Data inicial (DD-MM-YYYY): ")
    fim = input("Data final (DD-MM-YYYY): ")
    if not validar_data(inicio) or not validar_data(fim):
        erro("Formato de data inválido. Use DD-MM-YYYY.")
        return

    despesas = get_despesas()
    inicio_dt = datetime.strptime(inicio, "%d-%m-%Y")
    fim_dt = datetime.strptime(fim, "%d-%m-%Y")

    filtradas = [
        d for d in despesas
        if inicio_dt <= datetime.strptime(d["data"], "%d-%m-%Y") <= fim_dt
    ]
    exibir_despesas(filtradas)

def total_despesas_por_categoria():
    despesas = get_despesas()
    categorias = get_categorias()
    totais = {cat["nome"]: 0 for cat in categorias}
    for despesa in despesas:
        for cat in categorias:
            if despesa["categoria_id"] == cat["id"]:
                totais[cat["nome"]] += despesa["valor"]
    exibir_relatorio(totais)

def gerar_relatorio_mes_atual():
    despesas = get_despesas()
    categorias = get_categorias()
    mes_atual = datetime.now().strftime("%m-%Y")

    totais = {cat["nome"]: 0 for cat in categorias}
    for despesa in despesas:
        data_despesa = datetime.strptime(despesa["data"], "%d-%m-%Y")
        if data_despesa.strftime("%m-%Y") == mes_atual:
            for cat in categorias:
                if despesa["categoria_id"] == cat["id"]:
                    totais[cat["nome"]] += despesa["valor"]

    exibir_relatorio(totais)

def exibir_despesas_pendentes():
    despesas = get_despesas()
    pendentes = [d for d in despesas if d["status"].lower() == "pendente"]
    exibir_despesas(pendentes)