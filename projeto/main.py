from view import exibir_menu
import controller

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            controller.cadastrar_categoria()
        elif opcao == '2':
            controller.registrar_despesa()
        elif opcao == '3':
            controller.consultar_despesas_por_periodo()
        elif opcao == '4':
            controller.total_despesas_por_categoria()
        elif opcao == '5':
            controller.gerar_relatorio_mes_atual()
        elif opcao == '6':
            controller.exibir_despesas_pendentes()
        elif opcao == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
