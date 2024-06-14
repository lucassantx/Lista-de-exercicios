def ler_matriz():
    matriz = []
    for _ in range(3):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz

def soma_abaixo_diagonal_principal(matriz):
    soma = 0
    for i in range(1, 3):
        for j in range(i):
            soma += matriz[i][j]
    return soma

matriz = ler_matriz()

soma = soma_abaixo_diagonal_principal(matriz)

print("Soma dos elementos abaixo da diagonal principal:", soma)