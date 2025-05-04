from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV")
        print("Desligada!")


class ControleARCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado ...")
        print("Ar Condicionado Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado")
        print("Ar Condicionado Desligado!")


controle = ControleTV()
controle.ligar()
controle.desligar()


controle = ControleARCondicionado()
controle.ligar()
