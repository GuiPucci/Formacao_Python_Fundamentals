class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Resmovendo a instancia da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amrelo")
c.falar()

print("Olá mundo!")

del c

print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")

# criar_cachorro()
