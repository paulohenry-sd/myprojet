#atividade 04/03/2026 questao 1
time = input("digite o nome do time: ")
posiçâo = int(input("digite a posição do time na tabela (1 a 20): "))

if posiçâo == 1:
    print("campeâo")
elif posiçâo >= 2 and posiçâo <= 6:
    print("libertadores!")
elif posiçâo >= 7 and posiçâo <= 12:
    print("sul-americana!")
elif posiçâo >= 13 and posiçâo <= 16:
    print("meio da tabela.")
elif posiçâo >= 17 and posiçâo <= 20:
    print("rebaixado!")
else:
    print("posiçâo invalida!")
    