class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim plim ...")

    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm ...")

    # def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valo={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.modelo, b1.cor, b1.ano, b1.valor)
print(b1)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar()
b2.correr()
b2.parar()
print(b2.modelo, b2.cor, b2.ano, b2.valor)
print(b2)
