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
                self.adicionar_cliente(gerenciador)
            elif opcao == '2':
                self.buscar_cliente(gerenciador)
            elif opcao == '3':
                self.atualizar_cliente(gerenciador)
            elif opcao == '4':
                self.deletar_cliente(gerenciador)
            elif opcao == '5':
                gerenciador.listar_clientes()
            elif opcao == '6':
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção de 1 a 6.")

    def adicionar_cliente(self, gerenciador):
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input("Digite o e-mail (ou Enter para deixar em branco): ") or None
        telefone = input("Digite o telefone (ou Enter para deixar em branco): ") or None
        endereco = input("Digite o endereço (ou Enter para deixar em branco): ") or None
        gerenciador.adicionar_cliente(nome, idade, email, telefone, endereco)

    def buscar_cliente(self, gerenciador):
        chave = input("Digite o CPF do cliente para buscar: ")
        gerenciador.buscar_cliente(chave)

    def atualizar_cliente(self, gerenciador):
        chave = input("Digite o CPF do cliente para atualizar: ")
        gerenciador.atualizar_cliente(chave)

    def deletar_cliente(self, gerenciador):
        chave = input("Digite o CPF do cliente para deletar: ")
        gerenciador.deletar_cliente(chave)

