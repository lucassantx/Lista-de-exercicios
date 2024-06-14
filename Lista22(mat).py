def ler_matriz():
    matriz = []
    for i in range(3):
        linha = list(map(int, input(f"Digite os 3 valores da linha {i + 1} (separados por espaço): ").split()))
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(A, B):
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
    return C

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem}" for elem in linha))

print("Digite os valores da matriz A:")
A = ler_matriz()

print("\nDigite os valores da matriz B:")
B = ler_matriz()

C = multiplicar_matrizes(A, B)

print("\nMatriz resultante C = A * B:")
imprimir_matriz(C)