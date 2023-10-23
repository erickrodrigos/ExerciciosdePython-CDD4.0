class Pessoa:
    def __init__(self,Nome,Peso,Idade):
        # MÉTODOS CONTRUTORES
        # self.(parametro) = variável
        self.Nome = Nome
        self.Peso = Peso
        self.Idade = Idade
        self.Dormindo = False
        self.Comendo = False
        self.Falando = False
        self.Andando = False

    def Falar(self):
        if self.Dormindo == True:
            print(f" {self.Nome} não pode falar agora pois está dormindo")
        elif self.Comendo == True:
            print(f"  {self.Nome} NÃO PODE FALAR AGORA PQ ESTÁ COMENDO ")
        elif self.Falando == True:
            print(f"  {self.Nome} já está falando ")
        elif self.Andando == True:
             print(f"  {self.Nome} NÃO PODE FALAR AGORA PQ ESTÁ Andando ")
        else:
            print(f"{self.Nome} está falando")
            self.Falando = True

    def Comer(self,comida):
        if self.Dormindo == True:
            print(f" {self.Nome} não pode COMER agora pois está dormindo")
        elif self.Falando == True:
            print(f"  {self.Nome} NÃO PODE comer AGORA PQ ESTÁ FALANDO ")
        elif self.Comendo == True:
            print(f"  {self.Nome} já está comendo ")
        elif self.Andando == True:
            print(f"  {self.Nome} NÃO PODE Comer AGORA PQ ESTÁ Andando ")
        else:
            print(f"{self.Nome} está Comendo {comida}")
            self.Comendo = True

    def Dormir(self):
        if self.Falando == True:
            print(f" {self.Nome} não pode Dormir agora pois está FALANDO")
        elif self.Comendo == True:
             print(f"  {self.Nome} NÃO PODE DORMIR AGORA PQ ESTÁ COMENDO ")
        elif self.Dormindo == True:
             print(f"  {self.Nome} JÁ ESTÁ DORMINDO")
        elif self.Andando == True:
             print(f"  {self.Nome} NÃO PODE DORMIR AGORA PQ ESTÁ Andando ")
        else:
             print(f"{self.Nome} está DORMINDO")
             self.Dormindo = True
    def Andar(self):
        if self.Dormindo == True:
            print(f" {self.Nome} não pode dormir agora pois está andando")
        elif self.Comendo == True:
            print(f"  {self.Nome} NÃO PODE andar AGORA PQ ESTÁ Comendo ")
        elif self.Falando == True:
            print(f"  {self.Nome} NÃO PODE FALAR AGORA PQ ESTÁ ANDANDO ")
        else:
            print(f"{self.Nome} está Andando")
            self.Andando = True
    def PararFalar(self):
        if self.Falando == True:
            print(f"{self.Nome}  Parou de Falar")
            self.Falando = False
    def PararComer(self):
        if self.Comendo == True:
            print(f"{self.Nome}  Parou de Comer")
            self.Comendo = False

    def PararDormir(self):
        if self.Dormindo == True:
            print(f"{self.Nome}  Parou de Dormir")
            self.Dormindo = False
    def PararAndar(self):
        if self.Andando == True:
            print(f"{self.Nome}  Parou de Andar")
            self.Andando = False

    def Apresentar(self,):
        print(f"olá, Eu sou {self.Nome} e eu tenho {self.Peso}kilos")

    def Condicao(self):
        print(f"{self.Nome} está {self.Comendo}")