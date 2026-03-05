# operaçâo de operadores logicos em condicionais...
print("O que voce vai fazer amanha?")
print("dormir / estudar / planejar")
MANHA = input()
print("O que voce vai fazer amanha a tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("voce precisa dizer o que vai fazer!")
else:
    if TARDE == "dormir" or TARDE == "jogar":
        print("voce esta desperdiçando o seu dia!")
    elif MANHA == "estudar" or TARDE == "treinar":
        print("que bom! voce irà se aperfeiçoar!")
    elif MANHA == "planejar" and TARDE == "trabalhar":
        print("para trabalhar melhor, devo planejar!")
    else:
        print("nâo combinamos estas açâos...")

print("tenha um bom dia!")