from scripts.cliente import Clientes
from scripts.validacoes_dados import Validador

class GerenciadorDeClientes:
    def __init__(self):
        self.clientes = {}
        self.cpf_invalido = set()  # Conjunto para armazenar CPFs inválidos

    def adicionar_cliente(self, nome: str, idade: int, email: str = None, telefone: str = None, endereco: str = None):
        while True:
            cpf = input("Digite o CPF (11 dígitos): ")
            try:
                # Valida CPF
                cpf = Validador.validar_cpf(cpf)

                if cpf in self.clientes:
                    print("Cliente com esse CPF já cadastrado!")
                    return  # Sai da função se o CPF já estiver cadastrado
                
                # Valida outros dados
                nome = Validador.validar_nome(nome)
                idade = Validador.validar_idade(idade)
                email = Validador.validar_email(email)
                telefone = Validador.validar_telefone(telefone)

                # Adiciona cliente
                novo_cliente = Clientes(nome, cpf, idade, email, telefone, endereco)
                self.clientes[cpf] = novo_cliente
                print("Cliente adicionado com sucesso!")
                return  # Sai da função após adicionar com sucesso

            except ValueError as e:
                print(f"Erro: {e}")
                if isinstance(e, ValueError) and "CPF" in str(e):
                    self.cpf_invalido.add(cpf)

                if input("Deseja tentar novamente? (s/n): ").strip().lower() != 's':
                    print("Saindo do processo de adição de cliente.")
                    return

    def buscar_cliente(self, chave: str):
        """Busca um cliente pelo CPF."""
        cliente = self.clientes.get(chave)
        if cliente:
            print(cliente)
        else:
            print("Cliente não encontrado.")

    def atualizar_cliente(self, chave: str):
        """Atualiza as informações de um cliente."""
        cliente = self.clientes.get(chave)
        if cliente:
            print(f"Informações atuais: {cliente}")
            nome = input("Digite o novo nome (ou Enter para manter): ") or cliente.nome
            idade = input("Digite a nova idade (ou Enter para manter): ") or cliente.idade
            telefone = input("Digite o novo telefone (ou Enter para manter): ") or cliente.telefone
            email = input("Digite o novo e-mail (ou Enter para manter): ") or cliente.email
            endereco = input("Digite o novo endereço (ou Enter para manter): ") or cliente.endereco

            try:
                cliente.atualizar(nome, idade, email=email, telefone=telefone, endereco=endereco)
                print("Cliente atualizado com sucesso!")
            except ValueError as e:
                print(f"Erro ao atualizar cliente: {e}")
        else:
            print("Cliente não encontrado.")

    def deletar_cliente(self, chave: str):
        """Deleta um cliente pelo CPF."""
        if chave in self.clientes:
            del self.clientes[chave]
            print("Cliente deletado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def listar_clientes(self):
        """Lista todos os clientes cadastrados."""
        if self.clientes:
            for cliente in self.clientes.values():
                print(cliente)
        else:
            print("Nenhum cliente cadastrado.")

