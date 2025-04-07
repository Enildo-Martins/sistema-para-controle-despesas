from colorama import init, Fore, Style

init(autoreset=True)

def exibir_menu():
    print(Fore.CYAN + "\n--- Sistema de Controle de Despesas Pessoais ---")
    print("1. Cadastrar categoria de despesa")
    print("2. Registrar nova despesa")
    print("3. Consultar despesas por período")
    print("4. Exibir total de despesas por categoria")
    print("5. Gerar relatório do mês atual")
    print("6. Exibir despesas pendentes")
    print("0. Sair")

def exibir_categorias(categorias):
    print(Fore.YELLOW + "\nCategorias:")
    for categoria in categorias:
        print(f"{categoria['id']}: {categoria['nome']}")

def exibir_despesas(despesas):
    print(Fore.YELLOW + "\nDespesas:")
    for despesa in despesas:
        status_color = Fore.GREEN if despesa['status'].lower() == 'paga' else Fore.RED
        print(f"{Fore.WHITE}ID: {despesa['id']} | Valor: R${despesa['valor']} | "
              f"Data: {despesa['data']} | Categoria ID: {despesa['categoria_id']} | "
              f"Descrição: {despesa['descricao']} | "
              f"Status: {status_color}{despesa['status']}")

def exibir_relatorio(relatorio):
    print(Fore.MAGENTA + "\nRelatório:")
    for categoria, total in relatorio.items():
        print(f"{categoria}: R${total:.2f}")

def mensagem(msg):
    print(Fore.GREEN + f"\n{msg}")

def erro(msg):
    print(Fore.RED + f"\nErro: {msg}")