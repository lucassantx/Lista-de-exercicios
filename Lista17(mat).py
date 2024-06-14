def ler_notas_alunos():
    matriz = []
    for i in range(10):
        linha = list(map(float, input(f"Digite as notas das 3 provas do aluno {i + 1} (separadas por espaço): ").split()))
        matriz.append(linha)
    return matriz

def contar_piores_notas(matriz):
    piores_notas = [0, 0, 0]
    for notas in matriz:
        pior_prova = notas.index(min(notas))
        piores_notas[pior_prova] += 1
    return piores_notas

matriz_notas = ler_notas_alunos()

piores_notas = contar_piores_notas(matriz_notas)

print(f"Número de alunos cuja pior nota foi na prova 1: {piores_notas[0]}")
print(f"Número de alunos cuja pior nota foi na prova 2: {piores_notas[1]}")
print(f"Número de alunos cuja pior nota foi na prova 3: {piores_notas[2]}")