def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def matriz_maiores_valores(matriz1, matriz2):
    matriz_resultante = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(max(matriz1[i][j], matriz2[i][j]))
        matriz_resultante.append(linha)
    return matriz_resultante

matriz1 = []
print("Digite os elementos da primeira matriz 4x4:")
for _ in range(4):
    linha = list(map(int, input().split()))
    matriz1.append(linha)

matriz2 = []
print("Digite os elementos da segunda matriz 4x4:")
for _ in range(4):
    linha = list(map(int, input().split()))
    matriz2.append(linha)

matriz_maiores = matriz_maiores_valores(matriz1, matriz2)

print("\nMatriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
imprimir_matriz(matriz2)

print("\nMatriz com os maiores valores de cada posição:")
imprimir_matriz(matriz_maiores)