# demonstração de metodos em listas...
INSS = ["Maria", "manoel", "jode", "isabela"]
print("Eis, a fila do INSS:", INSS)

NOVO = input("insira mais uma pssoa: ")
INSS.append (NOVO)
print("conferindo a nova lista ", INSS)

print("vou tirar a ultima pessoa desta lista...")
ESPECIAL = INSS.pop()

print("Agora, vou coloca-la na frente de todos!")
INSS.insert(0, ESPECIAL)
print("Conferindo a lista: ", INSS)

print("maria não gostou e reclamou...")
INSS.remove("maria")
print("E agora, ela saiu 'pê da vida'", INSS)

print("para não ter mais reclação, vamos atender...")
INSS.sort()
print("... em ordem alfabetica:", INSS)

print("Onde está esta pessoa chamada", ESPECIAL, "?")
print("Ela agora ficou na posição", INSS.index(ESPECIAL)+1, "!")