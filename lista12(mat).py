def ler_matriz():
    matriz = []
    for _ in range(3):
        linha = list(map(int, input("Digite os elementos da linha separados por espaço: ").split()))
        matriz.append(linha)
    return matriz

def transposta_matriz(matriz):
    transposta = []
    for i in range(3):
        linha_transposta = []
        for j in range(3):
            linha_transposta.append(matriz[j][i])
        transposta.append(linha_transposta)
    return transposta

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

matriz = ler_matriz()

transposta = transposta_matriz(matriz)

print("Matriz transposta:")
imprimir_matriz(transposta)