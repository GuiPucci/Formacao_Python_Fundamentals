while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break
        print(numero)
        print()



for numero in range(100):
    if numero == 10:
        break
       
       
    print(numero, end=" ") 
    print()  
        

for numero in range(100):
    if numero % 2 == 0:
        continue
       
       
    print(numero, end=" ") 
    print()  


for numero in range(100):
    if numero % 2 != 0:
        continue
       
       
    print(numero, end=" ")  