def matriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(' '.join(map(str, linha)))

matriz = matriz()

print("Matriz:")
imprimir_matriz(matriz)