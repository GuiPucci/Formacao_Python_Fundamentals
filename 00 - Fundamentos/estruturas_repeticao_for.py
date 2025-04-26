#Exemplo utilizando um iterável
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print()





# Exemplo utilizando a função built-in range
number = int(input("Digite um número: "))
table_limit = (number * 10) + 1

print(f"Tabuada do {number}: ")

for i in range(0, table_limit, number):
        print(i, end=" ")
    