# demonstraçâo do uso do if...
print("digite a sua idade")
IDADE = int (input())


if IDADE < 18:
    print("você nâo è maior de idade!")
    print("nâo poderà realizar operaçês bancàrias!")
elif IDADE >= 65:
    print("voce jà esta ate aposentado .-.")
    print("vamos oferecer suporte tecnico, e tambem iremos mandar uma mensagem pro seu agente para ajudar com seus problemas bancarios...")
else:
    print("Você è maior de idade !")
    print("portanto, poderà realizar a operaçâo")

print("Obrigado por escolher os nossos serviços!")
