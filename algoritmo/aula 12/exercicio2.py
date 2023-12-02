idade_por_sobrenome= {}
for _ in range(5):
    sobrenome = input("Digite com Sobrenome")
    media_idades = int(input("Digite a idade"))
    idade_por_sobrenome[sobrenome] = media_idades

    idades = list(idade_por_sobrenome.values())
    media_idades = sum(idades) / len(idades)
    print(f"a media das idades é {media_idades}")

    for chave, valor in idade_por_sobrenome.items():
        if valor > media_idades:
            print(f"sobrenome: {chave}")