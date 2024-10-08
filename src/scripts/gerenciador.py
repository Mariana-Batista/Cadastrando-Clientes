from scripts.cliente import Clientes

class GerenciadorDeClientes:
    def __init__(self):
        self.clientes = {}
        self.cpf_invalido = set()  # Conjunto para armazenar CPFs inválidos

    def validar_cpf(self, cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        return True

    def adicionar_cliente(self, nome, idade, email=None, telefone=None):
        while True:
            cpf = input("Digite o CPF (11 dígitos): ")

            if not self.validar_cpf(cpf):
                if cpf not in self.cpf_invalido:  # Verifica se o CPF já foi digitado
                    print("CPF inválido! O CPF deve ter 11 dígitos.")
                    self.cpf_invalido.add(cpf)  # Adiciona o CPF inválido ao conjunto
                else:
                    print("Esta sequência numérica já foi digitada e é inválida.")
                
                opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()
                if opcao != 's':
                    print("Saindo do processo de adição de cliente.")
                    return  # Sai da função se o usuário não quiser tentar novamente
            else:
                if cpf in self.clientes:
                    print("Cliente com esse CPF já cadastrado!")
                    return  # Sai da função se o CPF já estiver cadastrado
                
                try:
                    novo_cliente = Clientes(nome, cpf, idade, email, telefone)
                    self.clientes[cpf] = novo_cliente
                    print("Cliente adicionado com sucesso!")
                    return  # Sai da função após adicionar com sucesso

                except ValueError as e:
                    print(f"Erro ao adicionar o cliente: {e}. Verifique os dados fornecidos.")
                    return  # Sai da função em caso de erro
            
    def buscar_cliente(self, chave):
        cliente = self.clientes.get(chave)
        if cliente:
            print(cliente)
        else:
            print("Cliente não encontrado.")

    def atualizar_cliente(self, chave):
        cliente = self.clientes.get(chave)
        if cliente:
            print(f"Informações atuais: {cliente}")
            nome = input("Digite o novo nome (ou Enter para manter): ")
            idade = input("Digite a nova idade (ou Enter para manter): ")
            telefone = input("Digite o novo telefone (ou Enter para manter): ")
            email = input("Digite o novo e-mail (ou Enter para manter): ")
            endereco = input("Digite o novo endereço (ou Enter para manter): ")

            try:
                cliente.atualizar(nome or None, idade or None, email=email or None, telefone=telefone or None, endereco=endereco or None)
                print("Cliente atualizado com sucesso!")
            except ValueError as e:
                print(f"Erro ao atualizar cliente: {e}")
        else:
            print("Cliente não encontrado.")

    def deletar_cliente(self, chave):
        if chave in self.clientes:
            del self.clientes[chave]
            print("Cliente deletado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def listar_clientes(self):
        if self.clientes:
            for cliente in self.clientes.values():
                print(cliente)
        else:
            print("Nenhum cliente cadastrado.")