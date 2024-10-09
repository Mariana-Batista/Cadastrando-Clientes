class Validador:
    @staticmethod
    def validar_nome(nome):
        # Verifica se o nome contém apenas letras e espaços (para nomes compostos)
        if not all(c.isalpha() or c.isspace() for c in nome):
            raise ValueError("O nome deve conter apenas letras do alfabeto.")
        return nome
    
    @staticmethod
    def validar_idade(idade):
        try:
            idade = int(idade)
            # Verifica se a idade é maior que 18
            if idade < 18:
                raise ValueError("A idade inserida é inválida! Deve ser maior que 18 anos.")
        except ValueError:
            raise ValueError("A idade inserida é inválida! Deve ser um número inteiro.")
        
        return idade  # Retorna a idade válida
    
    @staticmethod
    def validar_cpf(cpf):
        # Remove espaços antes e depois e verifica se o CPF tem 11 dígitos
        cpf = cpf.strip()
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError(f"CPF {cpf} é inválido! O CPF deve ter 11 dígitos.")
        return cpf  # Retorna o CPF válido
    
    @staticmethod
    def validar_email(email):
        # Verifica se o email contém '@' e um domínio simples
        if email and ("@" not in email or "." not in email.split("@")[-1]):
            raise ValueError("E-mail inválido! Verifique o formato.")
        return email  # Retorna o email válido

    @staticmethod
    def validar_telefone(telefone):
        # Remove espaços antes e depois e verifica se o telefone tem 11 dígitos
        telefone = telefone.strip()
        if len(telefone) != 11 or not telefone.isdigit():
            raise ValueError(f"O telefone {telefone} é inválido! O telefone deve conter 11 dígitos.")
        return telefone  # Retorna o telefone válido

    