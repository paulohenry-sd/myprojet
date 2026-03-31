#demonstraçâo de funçôes em listas...
print("Eis, os meus maiores sonhos..")
SONHOS = ["1. e divertir na disney",
          "2. me banhar na praia de sepetiba",
          "3. tirar as ferias em paris",
          "4. fazer compras no westshopping",
          "5. ver as piramides do egito"]
for X in SONHOS:
    print(X)

print("Ops, não quero sepetiba!")
del(SONHOS [1])
print("E nem westshopping...")
del(SONHOS[2])

print("Conferindo os sonhos...")
for X in SONHOS:
    print(X)