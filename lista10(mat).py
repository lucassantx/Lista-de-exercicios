def ler_matriz():
    matriz = []
    for _ in range(3):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][i]
    return soma

matriz = ler_matriz()

soma = soma_diagonal_principal(matriz)

print("Soma dos elementos na diagonal principal:", soma)