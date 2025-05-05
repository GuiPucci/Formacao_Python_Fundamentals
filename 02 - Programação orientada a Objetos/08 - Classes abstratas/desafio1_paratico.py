# O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação Orientada a  Objetos (POO). A classe deve conter um método para realizar a operação de soma entre dois números inteiros,encapsulando assim a lógica matemática da adição.


class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def soma(self):
        return self._num1 + self._num2


num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora(num1, num2)

resultado = calc.soma()
print(resultado)
