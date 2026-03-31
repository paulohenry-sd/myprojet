#demonstraçâo de funções em listas...
NUMEROS = [7,2,9,6,5,0,3,8,1,4]
PALAVRAS = ["ola", "alô", "hei", "uau", "ops"]

print("Quantas variaveis possui:")
print("numeros:", len(NUMEROS))
print("palavras:", len(PALAVRAS))

print("Vamos reordenar estas listas?")
print(sorted(NUMEROS))
print(sorted(PALAVRAS))

print("O somatorio de numeros:", sum(NUMEROS))
print("Qual é o maior valor?", max(NUMEROS))
print("Qual é a primeira palavra?", min(PALAVRAS))