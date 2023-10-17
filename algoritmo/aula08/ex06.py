palavra = input("digite a palavra: ")
inverso_palavra = palavra[::-1]
if palavra.lower() == inverso_palavra.lower():
    print(f"a palavra {palavra} é palindroma! ")
else:
    print(f"a palavra {palavra} NÃO é palindroma! ")


