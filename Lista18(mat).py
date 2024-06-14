def ler_matriz():
    matriz = []
    for i in range(3):
        linha = list(map(int, input(f"Digite os elementos da linha {i + 1} (separados por espaço): ").split()))
        matriz.append(linha)
    return matriz

def gerar_somas_colunas(matriz):
    soma_colunas = [0] * 3
    for i in range(3):
        for j in range(3):
            soma_colunas[j] += matriz[i][j]
    return soma_colunas

matriz = ler_matriz()

soma_colunas = gerar_somas_colunas(matriz)

print("Array das somas das colunas:", " ".join(map(str, soma_colunas)))