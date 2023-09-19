valor = float(input("Valor da sua compra: R$ "))

if valor <= 1000.00:
    desconto = valor * 0.10

elif valor <= 5000.00:
    desconto = valor * 0.20
    
else: 
    desconto = valor * 0.30
valor_final = valor - desconto

print(f"desconto: R$ {desconto:8.2f}")