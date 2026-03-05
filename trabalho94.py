#atividade 04/03/2026 questâo 3

a = float(input("digite o primeiro lado: "))
b = float(input("digite o segundo lado: "))
c = float(input("digite o segundo lado: "))

if a == b and b == c:
    print("triângulo Equilatero")
elif a == b or a == c or b == c:
    print("triangulo isosceles")
else:
    print("triangulo escaleno")
