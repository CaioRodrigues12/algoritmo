# Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro passado por parâmetro for par, e F (falso) se não.

def ehpar(numero):
    if (numero % 2) == 0:
        return True
    else:
        return False

x = int(input("Digite um Valor: "))
if ehpar(x):
    print(f"O número {x} é par! ")
else:
    print(f"O número {x} é impar! ")
