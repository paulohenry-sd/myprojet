# trabalho 2 algaritimos 02/03/2026 exercicio 

nome = input("digite o nome do filme que voce viu:")

print("digite a nota que vc deu ao filme:")
print("1. estrela")
print("2. estrelas")
print("3. estrelas")
print("4. estrelas")
print("5. estrelas")
ESTADO = int (input())

match ESTADO:
    case 1:
        print(" voce escolheu 2 estrelas, achou ruim dms...")
    case 2:
        print(" voce escolheu 2 estrelas, nao gostou tanto mas estava ok")    
    case 3:
        print("voce escolheu 3 estrelas, esse filme foi bom!")
    case 4:
        print("voce escolheu 4 estrelas, o filme foi incrivel!!!")
    case 5:
        print("voce escolheu 5 estrelas, o filme foi quase perfeito")
    case _:
        print("opçâo nâo reconhecida. escolha um dos numeros para colocar uma opçâo acima, de 1 a 5") 

 

print("Obrigado pelo feedback")
