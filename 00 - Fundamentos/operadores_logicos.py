# Exemplo de uso de operadores lógicos
# AND = para ser True todas as condições precisam ser True
# OR = para ser True apenas uma condição precisa ser True
# NOT = inverte o valor lógico da condição

print(True and True) # True
print(True and False) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or False) # False
print(not True) # False
print(not False) # True


saldo = 1000 # saldo da conta
saque = 250 # valor do saque
limite = 200 # limite de saque
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
print(exp) 

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)
print(conta_normal_com_saldo_suficiente)
print(conta_especial_com_saldo_suficiente)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
