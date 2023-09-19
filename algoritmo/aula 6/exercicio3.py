largura = float(input("Adicione a largura do local: "))
comprimento = float(input("Adicione o comprimento do local: "))
material = str(input("Qual será o material utilizado: "))
lata = 18
galao=3.6
litro = 1
altura = 2.80
areaparede = ((altura * largura) * 2) + ((altura * comprimento) * 2)
porta = 2.10 * 0.80
rendimentolitro = 3
quantidadelitro = ((areaparede - porta) / rendimentolitro) 

import math   
lata = (quantidadelitro/18)
lata_arredondado = math.ceil(lata)
galao = (quantidadelitro/3.6)
galao_arredondado = math.ceil (galao)
litrotinta = math.ceil (quantidadelitro)

if material == "lata":
    print(f"Será necessário {lata_arredondado} latas de 18L para a pintura das paredes") 
elif material == "galao":
    print(f"Será necessário {galao_arredondado} galões de 3,6L para pintura das paredes") 
else:
    print(f"Será necessário {litrotinta} litros para realizar a pintura das paredes")