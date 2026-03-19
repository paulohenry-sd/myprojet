#trabalho 1 dia 18/03/2026 (aula 9)

def APRESENTAR():
    print(f"minha idade è {Myage}.")
    return
def CONFERIR(X):
    if X >= 18:
        print("uma lista de veiculos a venda: Renault Kwid — cerca de R$ 80.000 |Fiat Mobi — cerca de R$ 80.000 | Citroën C3 — cerca de R$ 70.000 a R$ 80.000 |Peugeot 208 — cerca de R$ 88.000 | Hyundai HB20 — cerca de R$ 86.000")

    else:
        print("aqui esta uma lista de desenhos! Peppa Pig, Patrulha Canina, Bob Esponja, Galinha Pintadinha, Dora, a Aventureira, tartarugas ninjas, Turma da Mônica, apenas um Show, Backyardigans, Ben 10")
    return

Myage = int(input("digite sua idade: "))

APRESENTAR()
CONFERIR(Myage)