#atividades 04/03/2026 questão 4 

posiçâo = str(input("qual posiçâo voce pode exercer em um jogo de futebol?"))

if posiçâo == "goleiro" or posiçâo == "zagueiro" or posiçâo == "lateral":
    print("você joga na defesa!")
elif posiçâo == "ala" or posiçâo == "volante" or posiçâo == "meia":
    print("você ta no meio-campo")
elif posiçâo == "ponta" or posiçâo == "atacante" or posiçâo == "centroavante":
    print("você ta no ataque")
else:
    print("teimoso!!!!!")
    print("so tem, goleiro, zagueiro, lateral, ala, meia, volante, atacante, centroavante, e ponta.")
