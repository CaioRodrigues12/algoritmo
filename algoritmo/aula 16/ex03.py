def calcular_soma_multiplicacao(numero):
    soma = 0
    multiplicacao = 1

    for a in numero:
        digito = int(a)
        soma += digito
        multiplicacao *= digito

    return soma, multiplicacao

numero = input("Digite seu RA: ")

soma, multiplicacao = calcular_soma_multiplicacao(numero)
print(f"Soma = {soma}")
print(f"Multiplicação = {multiplicacao}")