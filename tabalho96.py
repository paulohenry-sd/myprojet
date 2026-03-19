# tabalho 5 dia 04/03/2026 (aula 5)
print("digite o numero de estrelas que voce quer dar ao filme:")
print("1. uma estrela")
print("2. duas estrelas")
print("3. três estrelas")
print("4. quatro estrelas")
print("5. cinco estrelas")
ESTADO = int (input())

match ESTADO:
    case 1:
        print("foi um pessimo filme")
    case 2:
        print("o filme foi ruim")    
    case 3:
        print("o filme foi ok")
    case 4:
        print("o filme foi bom")
    case 5:
        print("o filme foi incrivel!")
    case _:
        print("opçâo nâo reconhecida. escolha um dos numeros para colocar uma opçâo acima (1,2,3...)")  