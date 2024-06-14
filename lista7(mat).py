def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def gerar_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            if i < j:
                linha.append(2 * i + 7 * j)
            elif i == j:
                linha.append(3 * i ** 2)
            else:
                linha.append(4 * i ** 3 + 5 * j ** 2 + 1)
        matriz.append(linha)
    return matriz

matriz = gerar_matriz()

print("Matriz 10x10:")
imprimir_matriz(matriz)