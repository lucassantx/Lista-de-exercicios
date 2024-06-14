def ler_matriz():
    matriz = []
    for i in range(3):
        linha = list(map(float, input(f"Digite os 6 valores da linha {i + 1} (separados por espaço): ").split()))
        matriz.append(linha)
    return matriz

def soma_elementos_colunas_impares(matriz):
    soma = 0
    for i in range(3):
        for j in range(6):
            if j % 2 != 0:
                soma += matriz[i][j]
    return soma

def media_colunas_segunda_quarta(matriz):
    soma_segunda = 0
    soma_quarta = 0
    for i in range(3):
        soma_segunda += matriz[i][1]
        soma_quarta += matriz[i][3]
    media_segunda = soma_segunda / 3
    media_quarta = soma_quarta / 3
    return (media_segunda + media_quarta) / 2

def substituir_coluna_seis(matriz):
    for i in range(3):
        soma_colunas_1_2 = matriz[i][0] + matriz[i][1]
        matriz[i][5] = soma_colunas_1_2
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:.2f}" for elem in linha))

matriz = ler_matriz()

soma_impares = soma_elementos_colunas_impares(matriz)
print(f"Soma dos elementos das colunas ímpares: {soma_impares:.2f}")

media_segunda_quarta = media_colunas_segunda_quarta(matriz)
print(f"Média aritmética dos elementos da segunda e quarta colunas: {media_segunda_quarta:.2f}")

matriz_modificada = substituir_coluna_seis(matriz)

print("\nMatriz modificada:")
imprimir_matriz(matriz_modificada)