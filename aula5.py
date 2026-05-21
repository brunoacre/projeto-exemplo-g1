
class ContaBancaria: 
    """
        Representa a classe conta de um banco e possui
        os atributos XX, e os métodos YY.
    """
    def __init__(self, numero, cliente, agencia = "0001"):
        """
            Construtor da classe precisa receber os parametros
            XX, sendo o parametro XX do tipo YY.
        """
        self.numero = numero
        self.saldo = 0.0
        self.cliente = cliente
        self.agencia = agencia

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Saque efetuado. Novo saldo {self.saldo}.")
        else:
            print(f"A conta não possui saldo suficiente.")
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"Deposito efetuado. Novo saldo {self.saldo}.")

    def __str__(self):
        return f"A conta {self.numero} pertence ao cliente {self.cliente.nome}, CPF {self.cliente.cpf} e possui saldo {self.saldo}."   


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.score = 500
    
    def __str__(self):
        return f"O cliente {self.nome} possui o CPF {self.cpf}."



#print(ContaBancaria.__doc__)
#help(ContaBancaria)
cliente_bruno = Cliente("Bruno Rezende", "99999999999")
conta1 = ContaBancaria("1000-1", cliente_bruno, "0002")
print(conta1)
conta1.depositar(1000.00)
conta1.sacar(2000.00)

cliente_hendrik = Cliente("Hendrik", "11111111111")
conta2 = ContaBancaria("2222-2", cliente_hendrik)
print(conta2)
conta2.depositar(50000.00)
conta2.sacar(10000.00)

