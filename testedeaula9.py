# demonstraçâo do uso de funçôes...
def APRESENTAR():
    print(f"meu nome è {Myname}.")
    print(f"minha altura è de {Myheigh} metros.")
    print(f"meu minha idade è {Myage} anos.")
    return
def CONFERIR(X):
    if X >= 18:
        print("você è maior de idade!")
    else:
        print("ops, menor de idade nâo pode!")
    return

Myname = str(input("digite seu nome: "))
Myheigh = float(input("digite sua altura: "))
Myage = int(input("digite sua idade: "))

APRESENTAR()
CONFERIR(Myage)