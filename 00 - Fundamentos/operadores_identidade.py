# Operadores Lógicos
# Operadores de Identidade
# Operadores de Identidade são usados para verificar se dois objetos são o mesmo objeto na memória.
# Eles são representados por 'is' e 'is not'.
# 'is' verifica se dois objetos são o mesmo objeto na memória.
# 'is not' verifica se dois objetos não são o mesmo objeto na memória.
# Exemplo de uso dos operadores de identidade:


saldo = 1000
limite = 500

print(saldo is limite)  # False, porque são objetos diferentes na memória
print(saldo is not limite)  # True, porque são objetos diferentes na memória


saldo = 1000
limite = 1000

print(saldo is limite)  # True, porque ambos referenciam o mesmo objeto na memória
print(saldo is not limite)  # False, porque ambos referenciam o mesmo objeto na memória
