class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # Construtor da classe que inicializa os atributos da conta
        self.__numero = numero  
        self.__titular = titular  
        self.__saldo = saldo  
        self.__limite = limite  

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
        return True

    def transfere(self, valor, destino):
        # Método que transfere um valor da conta atual para uma conta destino
        # Essa abordagem é usada quando quiser encapsular as operações de saque e depósito em métodos separados.
        self.saca(valor)
        destino.deposita(valor)

    def get_numero(self):
        # Método que retorna o número da conta
        return self.__numero

    @property
    def saldo(self):
        # Propriedade que retorna o saldo da conta
        return self.__saldo

    @property
    def titular(self):
        # Propriedade que retorna o titular da conta
        return self.__titular

    @property
    def limite(self):
        # Propriedade que retorna o limite de crédito da conta
        return self.__limite

    @limite.setter
    def limite(self, limite):
        # Setter para modificar o limite de crédito da conta
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        # Método estático que retorna um dicionário com os códigos dos bancos
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @staticmethod
    def codigo_banco():
        # Método estático que retorna o código do banco
        return "001"

# Criar duas instâncias da classe Conta
conta = Conta(123, "Nico", 1000.0, 2000.0)
conta2 = Conta(321, "Lou", 1500.0, 2000.0)

# Imprimir os códigos dos bancos usando o método estático codigos_bancos()
print("Os códigos dos bancos são {}".format(Conta.codigos_bancos()))

# Imprimir o código do banco usando o método estático codigo_banco()
print("O código do banco é {}".format(Conta.codigo_banco()))

# Imprimir o número da conta do titular usando o método get_numero()
print("O número da conta do titular é {}".format(conta.get_numero()))

# Imprimir o nome do titular da conta usando a propriedade titular
print("O nome do titular da conta é {}".format(conta.titular))

# Imprimir o saldo inicial do titular da conta usando a propriedade saldo
print("O Saldo inicial do titular da conta é {}".format(conta.saldo))

# Imprimir o limite da conta do titular usando a propriedade limite
print("O limite da conta do titular é {}".format(conta.limite))

conta.saca(200.0)

conta.deposita(300.0)

valor_transferencia = 500.0
conta.transfere(valor_transferencia, conta2)

conta.extrato()

conta2.extrato()
