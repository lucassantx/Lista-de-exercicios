import random

def gerar_matriz_4x4():
    matriz = []
    for _ in range(4):
        linha = [random.randint(1, 20) for _ in range(4)]
        matriz.append(linha)
    return matriz

def transformar_matriz_triangular_inferior(matriz):
    triangular_inferior = []
    for i in range(4):
        linha = []
        for j in range(4):
            if j > i:
                linha.append(0)
            else:
                linha.append(matriz[i][j])
        triangular_inferior.append(linha)
    return triangular_inferior

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

matriz = gerar_matriz_4x4()

print("Matriz original:")
imprimir_matriz(matriz)

matriz_triangular_inferior = transformar_matriz_triangular_inferior(matriz)

print("\nMatriz triangular inferior:")
imprimir_matriz(matriz_triangular_inferior)