d = {}
for _ in range(5):
    nome = input("Digite com Sobrenome")
    idade = int(input("Digite a idade"))
    d[nome] = idade

    maior_sobrenome=''
    maior_idade= 0


for chave, valor in d.items():
    if valor > maior_idade:
        maior_idade = valor
        maior_sobrenome = chave
print(f"O sobrenome com a maior idade é {maior_idade}")
