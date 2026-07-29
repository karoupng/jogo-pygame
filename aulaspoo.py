class Dog:
    # atributo da classe "Canidae", notar que ele não está acompanhado de self, é um atributo global da classe

    family = "Canidae"

    # init roda automaticamente assim que a classe cachorro é criada
    def __init__(self, age: int):  # definindo o atributo age como int
        self.age = age


# self passa a ser o objeto mimi
mimi = Dog(5)
caramelo = Dog(7)

print(f"A idade da Mimi é {mimi.age}")
print(f"A família da Mimi é {mimi.family}")
print(f"Caramelo é um objeto de qual classe? {caramelo.__class__.__name__}")

# acesso público e privado no python, modificadores de acesso são
# diferentes de outras linguagens, não existem atributos verdadeiramente
#trancados em python

class ContaBancaria:
    def __init__(self, titular, saldo :int):
        self.titular = titular #Público
        self._agencia = "0001" #Protegido (1 underline)
        self.__saldo = saldo  #Privado (2 underlines)

conta = ContaBancaria("Karol",1000)
print(conta.titular)
conta.titular = "Ana"
