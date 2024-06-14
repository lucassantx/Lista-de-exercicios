def ler_matriz():
    matriz = []
    for i in range(3):
        linha = list(map(int, input(f"Digite os 3 valores da linha {i + 1} (separados por espaço): ").split()))
        matriz.append(linha)
    return matriz

def elevar_matriz_quadrado(A):
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                B[i][j] += A[i][k] * A[k][j]
    return B

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem}" for elem in linha))

print("Digite os valores da matriz A:")
A = ler_matriz()

B = elevar_matriz_quadrado(A)

print("\nMatriz resultante B = A^2:")
imprimir_matriz(B)