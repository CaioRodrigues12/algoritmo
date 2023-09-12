salario = float(input("Entre com seu salario: "))
percentual = float(input("Porcentagem de aumento: "))
valor_salario =  salario + (salario * percentual) / 100

print(f"seu salario é: , {valor_salario:8.2f}")