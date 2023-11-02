class Animal:
    def __init__(self, Nome, Cor, Som):
        self.Nome = Nome
        self.Cor = Cor
        self.Som = Som

    def comer(self):
        print(f"O {self.Nome} está comendo")

    def EmitirSom(self):
        print(f" o Animal {self.Nome} está {self.Som}")


class Gato(Animal):
    def __init__(self, Nome, Cor, Som):
        super().__init__(Nome, Cor, Som)

    def miar(self):

        print(f'O {self.Nome} está {self.Som}')

class Vaca(Animal):
    def __init__(self, Nome, Cor, Som):
        super().__init__(Nome, Cor, Som)

    def mugindo(self):

        print(f'O {self.Nome} está {self.Som}')


class Coelho(Animal):
    def __init__(self, Nome, Cor, Som):
        super().__init__(Nome, Cor, Som)

    def Calado(self):

        print(f'O {self.Nome} está {self.Som}')

class Cachorro(Animal):
    def __init__(self, Nome, Cor, Som):
        super().__init__(Nome, Cor, Som)

    def Latir(self):

        print(f'O {self.Nome} está {self.Som}')