import random

def gerar_cartela_bingo():
    numeros = random.sample(range(100), 25)
    cartela = [numeros[i*5:(i+1)*5] for i in range(5)]
    return cartela

def imprimir_cartela(cartela):
    for linha in cartela:
        print(" ".join(f"{num:2d}" for num in linha))

cartela = gerar_cartela_bingo()

print("Cartela de Bingo:")
imprimir_cartela(cartela)