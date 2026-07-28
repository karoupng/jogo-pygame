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

# acesso público e privado no python