#trabalho 2 dia 18/03/2026 (aula 9)

import random

escolha = int(input("Você quer par ou impar? coloque (1= impar 2=par):")).strip().lower()

jogador = int(input("Digite um número (0 a 10): "))

computador = random.randint(0, 10)

soma = jogador + computador
print(f"Soma = {soma}")

if soma % 2 == 0:
    resultado = "2"
    print("Deu par")
else:
    resultado = "1"
    print("Deu impar")

if escolha == resultado:
    print("Você ganhou")
else:
    print("Você perdeu")