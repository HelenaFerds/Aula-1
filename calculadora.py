variavel_1 = int(input("Digite o primeiro número:"))
variavel_2 = int(input("Digite o segundo numero:"))

soma = variavel_1 + variavel_2
subtracao = variavel_1 - variavel_2
multiplicacao = variavel_1 * variavel_2
divisao = variavel_1 / variavel_2

pergunta = input("Qual operação você deseja realizar? (soma, subtração, multiplicação, divisão):")

if pergunta == "soma":
    print("O resultado da soma é :",soma)
elif pergunta == "subtracao":
    print("O resultado da subtração é :",subtracao)
elif pergunta == "multiplicacao":
    print("O resultado da multiplicação é :", multiplicacao)
elif pergunta == "divisao":
    print("O resultado da divisão é :", divisao)
else: print("Operação invalida, tente novamente.")

