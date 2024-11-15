frase1 = input()
frase2 = input()

letra = ""

lista_palavras1 = frase1.split()  
lista_palavras2 = frase2.split() 

conjunto = set()  

for palavra in lista_palavras1:
    if palavra in lista_palavras2:
        conjunto.add(palavra)

for palavra in conjunto:
    letra += palavra 

letra = " ".join(conjunto)
letra = letra.replace("  ", " ")

print(letra)
