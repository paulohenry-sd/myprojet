#trabalho 2 dia 30/03/2026 (aual 9)

jogadores = []

print("=== Cadastro dos Jogadores Titulares ===")
for i in range(11):
    nome = input(f"Digite o nome do jogador {i+1}: ")
    numero = int(input(f"Digite o número da camisa de {nome}: "))
    jogadores.append({"nome": nome, "numero": numero})

print("\n=== Escalação Inicial ===")
for j in jogadores:
    print(f"{j['numero']} - {j['nome']}")

print("\n=== Intervalo: Substituições ===")
for i in range(3):
    resp = input("Deseja fazer uma substituição? (s/n): ").lower()
    
    if resp == 's':
        num_saida = int(input("Digite o número do jogador que vai sair: "))
        
        
        for j in jogadores:
            if j["numero"] == num_saida:
                jogadores.remove(j)
                break
        
        
        nome = input("Digite o nome do jogador que vai entrar: ")
        numero = int(input("Digite o número da camisa: "))
        jogadores.append({"nome": nome, "numero": numero})

print("\n=== Escalação Atualizada ===")
for j in jogadores:
    print(f"{j['numero']} - {j['nome']}")