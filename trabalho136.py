#trabalho 1 dia: 16/03/2026

numero = int(input("digite um numero entre 0 e 25: "))

if numero < 0 or numero > 25:
    print("numero recusado")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i

    print("o fatorial è:", fatorial)