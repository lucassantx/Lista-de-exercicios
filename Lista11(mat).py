def ler_matriz():
    matriz = []
    for _ in range(3):
        linha = list(map(int, input("Digite os elementos da linha separados por espaço: ").split()))
        matriz.append(linha)
    return matriz

def soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][2 - i]
    return soma

matriz = ler_matriz()

soma = soma_diagonal_secundaria(matriz)

print("Soma dos elementos na diagonal secundária:", soma)