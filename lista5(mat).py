def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

matriz = []
print("Digite os elementos da matriz 5x5:")
for _ in range(5):
    linha = list(map(int, input().split()))
    matriz.append(linha)

valor = int(input("Digite o valor a ser buscado na matriz: "))

print("\nMatriz:")
imprimir_matriz(matriz)

localizacao_valor = buscar_valor(matriz, valor)

if localizacao_valor:
    print("\nO valor", valor, "foi encontrado na posição:", localizacao_valor)
else:
    print("\nO valor", valor, "não foi encontrado na matriz.")