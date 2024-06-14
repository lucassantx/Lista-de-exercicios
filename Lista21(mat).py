def ler_matriz():
    matriz = []
    for i in range(2):
        linha = list(map(float, input(f"Digite os 2 valores da linha {i + 1} (separados por espaço): ").split()))
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz1, matriz2):
    matriz_soma = []
    for i in range(2):
        linha_soma = []
        for j in range(2):
            linha_soma.append(matriz1[i][j] + matriz2[i][j])
        matriz_soma.append(linha_soma)
    return matriz_soma

def subtrair_matrizes(matriz1, matriz2):
    matriz_subtracao = []
    for i in range(2):
        linha_subtracao = []
        for j in range(2):
            linha_subtracao.append(matriz1[i][j] - matriz2[i][j])
        matriz_subtracao.append(linha_subtracao)
    return matriz_subtracao

def adicionar_constante(matriz, constante):
    for i in range(2):
        for j in range(2):
            matriz[i][j] += constante

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:.2f}" for elem in linha))

# Leitura das duas matrizes
print("Digite os valores da primeira matriz:")
matriz1 = ler_matriz()

print("\nDigite os valores da segunda matriz:")
matriz2 = ler_matriz()

# Menu de opções
while True:
    print("\nMENU DE OPÇÕES:")
    print("a) Somar as duas matrizes")
    print("b) Subtrair a primeira matriz da segunda")
    print("c) Adicionar uma constante às duas matrizes")
    print("d) Imprimir as matrizes")
    print("e) Sair")

    opcao = input("\nEscolha uma opção (a, b, c, d ou e): ")

    if opcao == 'a':
        matriz_soma = somar_matrizes(matriz1, matriz2)
        print("\nMatriz resultante da soma:")
        imprimir_matriz(matriz_soma)
    elif opcao == 'b':
        matriz_subtracao = subtrair_matrizes(matriz1, matriz2)
        print("\nMatriz resultante da subtração:")
        imprimir_matriz(matriz_subtracao)
    elif opcao == 'c':
        constante = float(input("\nDigite a constante a ser adicionada: "))
        adicionar_constante(matriz1, constante)
        adicionar_constante(matriz2, constante)
        print("\nMatriz 1 após adição da constante:")
        imprimir_matriz(matriz1)
        print("\nMatriz 2 após adição da constante:")
        imprimir_matriz(matriz2)
    elif opcao == 'd':
        print("\nMatriz 1:")
        imprimir_matriz(matriz1)
        print("\nMatriz 2:")
        imprimir_matriz(matriz2)
    elif opcao == 'e':
        print("\nPrograma encerrado.")
        break
    else:
        print("\nOpção inválida. Escolha novamente.")