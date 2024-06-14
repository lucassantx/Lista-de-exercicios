linhas = 3
colunas = 3

matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = i * j

for linha in matriz:
    print(linha)