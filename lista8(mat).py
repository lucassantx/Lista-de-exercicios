def ler_matriz():
    matriz = []
    for _ in range(3):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz

def soma_acima_diagonal_principal(matriz):
    soma = 0
    for i in range(3):
        for j in range(i + 1, 3):
            soma += matriz[i][j]
    return soma

matriz = ler_matriz()

soma = soma_acima_diagonal_principal(matriz)

print("Soma dos elementos acima da diagonal principal:", soma)