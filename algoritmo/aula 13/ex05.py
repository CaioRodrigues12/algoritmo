

def ehprimo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def qtd_primos(n):
    qtd = 0
    for i in range(1, n+1):
        if ehprimo(i):
            qtd = qtd + 1
    return qtd

valor = int(input("entre com o número: "))
print(f"A quantidade de primos entre 1 e {valor} é: ")
print(f"{qtd_primos(valor)}")