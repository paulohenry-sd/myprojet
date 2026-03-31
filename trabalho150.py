# trabalho 1 dia 30/03/2026 (aula 9)


print("questão 1:", "qual seria a quantidade de patas de uma cobra?",
      "(a) 2", "(b) 0", "(c) 3", "(d) 100", "(e) 1")

print("questão 2:", "qual seria o numero de algarismos nesse exemplo (21636)",
      "(a) 10000", "(b) 1", "(c) 5", "(d) 90", "(e) 21636")

print("questão 3:", "se 20 pessoas fizeram uma prova e 5 passaram, qual a porcentagem?",
      "(a) 25%", "(b) 50%", "(c) 30%", "(d) 0,25%", "(e) 5%")

print("questão 4:", "papagaio imita 3 pessoas por vez, se passaram 27 pessoas?",
      "(a) 27", "(b) 12", "(c) 3", "(d) 9", "(e) 0")

print("questão 5:", "problema das pessoas no acampamento",
      "(a) 2", "(b) 10", "(c) 3", "(d) 5", "(e) 8")

gabarito = ['B', 'C', 'A', 'E', 'D']

respostas = []

for i in range(5):
    resp = input(f"Digite a resposta da questão {i+1}: ").upper()
    respostas.append(resp)

acertos = 0

for i in range(5):
    if respostas[i] == gabarito[i]:
        acertos += 1

print("Você acertou", acertos, "questões.")