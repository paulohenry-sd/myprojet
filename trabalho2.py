#tabralho 2 02/03/2026
nota1 = float(input("digite a sua preimeira nota: "))
nota2 = float(input("digite a sua segunda nota: "))
nota3 = float(input("digite a sua terceira nota: "))
nota4 = float(input("digite a sua quata nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("media", media)

if media < 6:
    print("reprovado")
else:
    print("aluno reprovado")
    