class Clientes:
    def __init__(self, nome, cpf, idade, email=None, telefone=None, endereco=""):
        if not email and not telefone:
            raise ValueError("É necessário fornecer pelo menos um meio de contato: e-mail ou telefone")
        
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco    
    
    def atualizar(self, nome, idade=None, email=None, telefone=None, endereco=None): 
        if not email and not telefone and not self.email and not self.telefone:
            raise ValueError("É necessário fornecer pelo menos um meio de contato: e-mail ou telefone")
        
        if nome:
            self.nome = nome
        if idade:
            self.idade = idade
        if email:
            self.email = email
        if telefone:   
            self.telefone = telefone
        if endereco:    
            self.endereco = endereco
    
    def __str__(self):
         return f"Nome: {self.nome} |  CPF: {self.cpf} | Idade: {self.idade} | E-mail: {self.email} | Telefone: {self.telefone} | Endereço: {self.endereco}"
    
        