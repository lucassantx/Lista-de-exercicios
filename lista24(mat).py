def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("\t".join(map(str, linha)))

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i] == [jogador] * 3 or [tabuleiro[j][i] for j in range(3)] == [jogador] * 3:
            return True

    if [tabuleiro[i][i] for i in range(3)] == [jogador] * 3 or [tabuleiro[i][2 - i] for i in range(3)] == [jogador] * 3:
        return True

    return False

def proxima_jogada(tabuleiro):
    possiveis_jogadas = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                possiveis_jogadas.append((i, j))

    for jogada in possiveis_jogadas:
        tabuleiro[jogada[0]][jogada[1]] = -1
        if verificar_vitoria(tabuleiro, -1):
            tabuleiro[jogada[0]][jogada[1]] = 0
            return jogada
        tabuleiro[jogada[0]][jogada[1]] = 0

    for jogada in possiveis_jogadas:
        tabuleiro[jogada[0]][jogada[1]] = 1
        if verificar_vitoria(tabuleiro, 1):
            tabuleiro[jogada[0]][jogada[1]] = 0
            return jogada
        tabuleiro[jogada[0]][jogada[1]] = 0

    import random
    return random.choice(possiveis_jogadas)

tabuleiro = [
    [-1, 1, 1],
    [-1, -1, 0],
    [0, 1, 0]
]

print("Tabuleiro atual:")
imprimir_tabuleiro(tabuleiro)

proxima = proxima_jogada(tabuleiro)
print("\nPróxima jogada sugerida:", proxima)