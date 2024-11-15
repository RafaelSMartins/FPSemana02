frase = input()
frase = ''.join(frase.split()) 
dicionario = {}

for letras in frase:
    if letras in dicionario:
        dicionario[letras] += 1
    else:
        dicionario[letras] = 1
 

print(dicionario)
