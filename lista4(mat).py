def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def localizar_maior_valor(matriz):
    maior_valor = matriz[0][0]
    localizacao = (0, 0)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                localizacao = (i, j)
                
    return localizacao

matriz = []
print("Digite os elementos da matriz 4x4:")
for _ in range(4):
    linha = list(map(int, input().split()))
    matriz.append(linha)

print("\nMatriz:")
imprimir_matriz(matriz)

localizacao_maior_valor = localizar_maior_valor(matriz)
print("\nA localização do maior valor é:", localizacao_maior_valor)