#demonstração de acesso a listas...

print("vou montar com 5 alimentos!")
MARMITA = ["seijâo", "arroz","legumes", "salada", "carne"]
print("Eis, a nossa recomendaçâo:", MARMITA)
RESPOSTA = input("Quer montar uma marmita diferente (S/N)?")
if RESPOSTA == "S":
    for X in range(len(MARMITA)):
        print(f'digite o {X+1}o. item do cardàpio')
        MARMITA[X] = input()
    print("A marmita montada foi:", MARMITA)
    print("O tres primeiros itens foram:", MARMITA[0:3])
    print("O ultimo item da marmita foi:", MARMITA [-1])
else:
    print("ok. você decide...")