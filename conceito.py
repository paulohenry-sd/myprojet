# notas 04/03/2026
NOTA = int(input("digite sua nota: "))
PRESENÇA = int(input("digite a porcentagem da sua presença"))

if NOTA >= 6 and PRESENÇA >= 75:
    print('aprovado')
elif NOTA < 6 and PRESENÇA < 75:
    print("reprovado")
else:
    print("recuperaçâo")