class Retangulo:

    def __init__(self, lado_a,lado_b):
        self.a = lado_a
        self.b = lado_b

    def muda_valor(self, novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b

    def retorna_lado(self):
        print(f'Dimensões do retângulo: {self.a}x{self.b}')

    def area(self):
        return self.a * self.b