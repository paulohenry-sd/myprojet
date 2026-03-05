# demonstraçâo do usoda condicional math/case...
print("digite o numero referente ao estado da moeda:")
print("1. flor de cunho")
print("2. soberba")
print("3. muito bem conservada")
print("4. bem conservada")
print("5. Outros estados")
ESTADO = int (input())

match ESTADO:
    case 1:
        print("perfeita! vou pagar R$ 1.000.000,00!")
    case 2:
        print("Quase perfeita! ofereço R$ 250.000,00!")    
    case 3:
        print("que òtimo! posso dar uns R$ 100.000,00!")
    case 4:
        print("que bom, aceitaria 30.004,00?")
    case 5:
        print("desculpe, nâo aceito neste estado")
    case _:
        print("opçâo nâo reconhecida. escolha um dos numeros para colocar uma opçâo acima")  