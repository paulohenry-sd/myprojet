#trabalho 4 dia 16/03/2026

valor = int(input("digite o valor para sacar: "))
cont50 = 0
cont20 = 0
cont10 = 0

while valor > 0:
    if valor >= 50:
        cont50 += 1
        valor -= 50
    elif valor >= 20:
        cont20 += 1
        valor -= 20
    elif valor >= 10:
        cont10 += 1
        valor -= 10
    else:
        print("valor inválido para saque (não múltiplo de 10)")
        break

print(f"irei receber {cont50} notas de 50, {cont20} notas de 20 e {cont10} notas de 10")