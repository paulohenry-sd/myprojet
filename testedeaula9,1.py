#demonstraçâo do uso de funçôes (aula nove, 18/03/2026)
def ADIÇÂO (X, Y):
    W = X + Y
    return W
def SUBTRAÇÂO(X, Y):
    return X - Y

print("digite dois valores inteiros...")
N1 = int(input("X: "))
N2 = int(input("Y: "))
OP = input("qual operaçâo (+ ou -)?")

if OP == "+":
    Z = ADIÇÂO(N1, N2)
    print("resultado da soma:", Z)
elif OP =="-":
    Z = SUBTRAÇÂO(N1, N2)
    print("resultado da suntraçâo", Z)
else:
    print("opçâo digitada inexistente!")