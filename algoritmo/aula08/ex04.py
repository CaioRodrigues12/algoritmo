frase = str(input("Digite uma Frase: "))
qtd = 0
for letra in frase:
    if letra.lower() in "aeiou":
        qtd = qtd + 1

print(f"a frase possui {qtd} vogais!")
