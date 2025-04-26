nome = "GUIlherME"

print(nome.upper()) # Converte todos os caracteres para maiúsculo
print(nome.lower()) # Converte todos os caracteres para minúsculo
print(nome.title()) # Converte a primeira letra de cada palavra para maiúsculo


texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")  # Remove espaços em branco no início e no final
print(texto.lstrip() + ".") # Remove espaços em branco no início
print(texto.rstrip() + ".") # Remove espaços em branco no final 


menu = ("Python")

print("####" + menu + "####") # Adiciona o caractere "#" no início e no final da string
print(menu.center(14)) # Adiciona espaços em branco para completar o tamanho total de 14 caracteres
print(menu.center(14, "#")) # Adiciona o caractere "#" para completar o tamanho total de 14 caracteres
print(menu.upper().center(14)) # Adiciona espaços em branco para completar o tamanho total de 14 caracteres e converte para maiúsculo
print("P-y-t-h-o-n")  
print("-".join(menu)) # Adiciona o caractere "_" entre cada letra da string
print("P-y-t-h-o-n".replace("-", " ")) # Substitui o caractere "-" por um espaço em branco    
