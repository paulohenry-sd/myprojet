#trabalho 3 02/03/2026

peso = float(input("digite seu peso (kg):"))
altura = float(input("digite sua altura (m):"))

IMC = peso / (altura * altura)

print("seu IMC è", IMC)

if IMC < 18:
    print("abaixo do peso ideal")
elif IMC > 25:
    print("acima do peso ideal")
else:
    print("seu peso esta bom")