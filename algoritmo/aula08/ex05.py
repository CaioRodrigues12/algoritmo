frase = (input("Digite uma Frase: "))
palavra = input("digite a palavra")

qtd = frase.count(palavra)
total_palavras = frase.count(" ") + 1

print(f"a frase possui um total de {total_palavras} palavras")
print(f"a palavra {palavra} foi encontrada {qtd} vezes na frase")