from scripts.gerenciador import GerenciadorDeClientes

class Menu:

    def exibir_menu(self):
        print("\nMenu de Opções:")
        print("1 - Adicionar Cliente")
        print("2 - Buscar Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Deletar Cliente")
        print("5 - Listar Clientes")
        print("6 - Sair")

    def executar_programa(self):
        gerenciador = GerenciadorDeClientes()

        while True:
            self.exibir_menu()  # Chama a função para exibir o menu
            opcao = input("\nEscolha uma opção (1-6): ")

            if opcao == '1':
                nome = input("Digite o nome: ")
                cpf = input("Digite o CPF: ")
                idade = input("Digite a idade: ")
                email = input("Digite o e-mail (ou Enter para deixar em branco): ")
                telefone = input("Digite o telefone (ou Enter para deixar em branco): ")
                gerenciador.adicionar_cliente(nome, cpf, idade, email or None, telefone or None)

            elif opcao == '2':
                chave = input("Digite o CPF do cliente para buscar: ")
                gerenciador.buscar_cliente(chave)

            elif opcao == '3':
                chave = input("Digite o CPF do cliente para atualizar: ")
                gerenciador.atualizar_cliente(chave)

            elif opcao == '4':
                chave = input("Digite o CPF do cliente para deletar: ")
                gerenciador.deletar_cliente(chave)

            elif opcao == '5':
                gerenciador.listar_clientes()

            elif opcao == '6':
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida! Por favor, escolha uma opção de 1 a 6.")