# Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa. Implemente um método para retornar uma representação formatada dos dados da pessoa, crie uma instância da pessoa e, por fim, chame o método para retornar as informações formatadas e imprimir o resultado. O objetivo é utilizarmos formas para criar e manipular objetos com POO, usando atributos e métodos para encapsular dados e comportamentos.


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

# TODO: Crie um método para retornar as informações formatas com Nome e Idade:

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


# Entrada do usuário
nome = input("Qual seu nome?: ")
idade = int(input("Qual sua idade?: "))

# TODO: Crie uma instância da pessoa:

pessoa = Pessoa(nome, idade)

# TODO: Chame o método para retornar as informações formatadas e imprima o resultado:

print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")
