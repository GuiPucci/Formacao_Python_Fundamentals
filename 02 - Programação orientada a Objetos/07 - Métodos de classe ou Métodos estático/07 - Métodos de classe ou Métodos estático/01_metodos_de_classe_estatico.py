# class Pessoa:
#    def __init__(self, nome=None, idade=None):
#        self.nome = nome
#        self.idade = idade
#
#    def criar_data_nascimento(self, ano, mes, dia, nome):
#        idade = 2025 - ano
#        return Pessoa(nome, idade)
#
#
# p = Pessoa("Guilherme", 36)
# print(p.nome, p.idade)
#
# p = Pessoa().criar_data_nascimento(1988, 6, 6, "Guilherme")
# print(p.nome, p.idade)


#########################################################################

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


# p = Pessoa("Guilherme", 36)
# print(p.nome, p.idade)

p = Pessoa.criar_data_nascimento(1988, 6, 6, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(8))
