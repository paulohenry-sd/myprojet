#trabalho 3 dia 18/03/2026 (aula 9)

def APRESENTAR():
    print(f"meu nome è {Myname}.")
    print(f"sou da cidade de {Myage}.")
    return
def CONFERIR(X):
    if X.lower() == "Rio de janeiro":
        print("  ")
    else:
        print("seja bem vindo a cidade maravilhosa")
    return

Myname = input("digite seu nome: ")
Myage = input("digite a cidade da onde esta vindo essa mensagem: ")

APRESENTAR()
CONFERIR(Myage)
