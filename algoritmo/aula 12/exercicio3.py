lista1 = []
lista2 = []

for i in range(1, 6):
    lista1.append(int(input(f"digite o {i} elem. 1a. lista: ")))
for i in range(1, 6):
    lista2.append(int(input(f"digite o {i} elem. 2a. lista2: ")))

conjunto_uniao = set(lista1).union(set(lista2))

print("Conjunto da uniao entre as duas listas: ")
print(conjunto_uniao)




