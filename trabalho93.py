#atividade 04/03/2026 questâo 2
X = int(input("digite o primeiro numero:"))
Y = int(input("digite o segundo numero: "))
Z = int(input("digite o terceiro numero:"))

if X < Y and Y < Z:
    print("estâo em ordem crescente!")
elif X > Y and Y > Z:
    print("estâo em ordem decrscente!")
else:
    print("eles estâo misturados, ou sâo infinitos e nâo da pra definir!")
