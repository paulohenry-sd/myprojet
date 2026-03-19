# trabalho 3 dia 16/03/2026

print("digite os numeros da megasena (numeros de 1 a 9)")

N1 = int(input("digite  primeiro numero: "))

N2 = int(input("digite  segundo numero: "))

if N2 == N1:
    print("voce colocou um numero repitido faça de novo")

N3 = int(input("digite  terceiro numero: "))

if N3 == N1 or N2:
    print("voce colocou um numero repitido faça de novo")

N4 = int(input("digite  quarto numero: "))

if N4 == N1 or N2 or N3:
    print("voce colocou um numero repitido")

N5 = int(input("digite  quinto numero: "))

if  N5 == N2 or N3 or N1 or N4:
    print("voce colocou um numero repitido")

N6 = int(input("digite  sexto numero: "))

if N6 == N2 or N3 or N4 or N5:
    print("voce colocou um numero repitido")

else:
    print("esses sâo seus numeros da telesena:", N1, N2, N3, N4, N5, N6)
    