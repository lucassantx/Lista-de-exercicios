def ler_matriz():
    matriz = []
    for i in range(5):
        linha = list(map(int, input(f"Digite o número de matrícula, a média das provas e a média dos trabalhos do aluno {i + 1} (separados por espaço): ").split()))
        linha.append(linha[1] + linha[2])
        matriz.append(linha)
    return matriz

def encontrar_maior_nota_final(matriz):
    maior_nota = -1
    matricula_maior_nota = -1
    for aluno in matriz:
        if aluno[3] > maior_nota:
            maior_nota = aluno[3]
            matricula_maior_nota = aluno[0]
    return matricula_maior_nota

def calcular_media_notas_finais(matriz):
    soma_notas_finais = sum(aluno[3] for aluno in matriz)
    media_notas_finais = soma_notas_finais / len(matriz)
    return media_notas_finais

matriz = ler_matriz()

matricula_maior_nota = encontrar_maior_nota_final(matriz)
media_notas_finais = calcular_media_notas_finais(matriz)

print(f"Matrícula do aluno com a maior nota final: {matricula_maior_nota}")
print(f"Média aritmética das notas finais: {media_notas_finais:.2f}")