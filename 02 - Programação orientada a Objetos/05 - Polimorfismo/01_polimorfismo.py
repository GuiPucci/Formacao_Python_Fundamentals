class Passaro:
    def voar(self):
        print(f"O {self.__class__.__name__} está Voando ...")


class Pardal(Passaro):
    def voar(self):
        print("O Pardal pode voar")
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print(f"O {self.__class__.__name__} não pode voar")


# FIXME: exemplo ruim de uso de erança para "ganhar o método voar"
class Aviao(Passaro):
    def voar(self):
        print(f"O {self.__class__.__name__} está decolando")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
