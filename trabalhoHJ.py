# Construa e aprenda saldo

print("digite o saldo da sua conta bancaria:")
saldo = float (input())

print("digite o valor do produto que quer comprar:")
produto = float (input())

Valor = saldo - produto
if saldo >= produto:
    print("o saldo è suficiente para a compra.")
    print("e sobrarà:", Valor)
else:
    print("o saldo è insuficiente para a compra.")
    print("è necessario ter no minimo:", produto)
