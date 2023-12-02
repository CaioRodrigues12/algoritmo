from math import pow, pi


def calcula_volume(raio):
    return ((4 / 3) * pi * pow(raio, 3))

r = float(input("Entre com o valor do raio: "))

print(f"o volume da esfera é {calcula_volume(r):.3f}³")
