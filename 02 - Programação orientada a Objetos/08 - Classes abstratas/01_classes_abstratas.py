from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # @abstractproperty - O decorador @abstractproperty aparece riscado (deprecado) porque ele está obsoleto nas versões mais recentes do Python. Esse decorador foi substituído por uma combinação de @property com @abstractmethod.
    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"


class ControleARCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado ...")
        print("Ar Condicionado Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado")
        print("Ar Condicionado Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleARCondicionado()
controle.ligar()
print(controle.marca)