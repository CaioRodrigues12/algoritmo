comprimento = float(input("Digite o comprimento da parede: "))
largura = float(input("Digite a largura da parede: "))
material = str(input("digite qual a opçao de material que sera usada:"))
altura = 2.8
porta = 0.8 * 2.10
lata = 18
galao = 3.6
litro = 1

total_pintura = ((comprimento * altura) + (largura * altura) * 2) - porta

tinta = total_pintura / 3

import math   
lata = (litro/18)
lata_arredondado = math.ceil(lata)
galao = (litro/3.6)
galao_arredondado = math.ceil (galao)
litro = math.ceil (litro)

if material == "lata":
    print(f"Será necessário {lata_arredondado} latas de 18L para pintar o cômodo") 
elif material == "galao":
    print(f"Será necessário {galao_arredondado} galões de 3,6 Lpara pintar o cômodo") 
else:
    print(f"Será necessário {litro} litros para realizar a pintura do cômodo")

