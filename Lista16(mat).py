def ler_gabarito():
    gabarito = input("Digite o gabarito (10 respostas separadas por espaço, opções: a, b, c, d ou e): ").split()
    return gabarito

def ler_respostas_alunos():
    alunos = []
    for i in range(3):
        matricula = int(input(f"Digite a matrícula do aluno {i + 1}: "))
        respostas = input(f"Digite as respostas do aluno {i + 1} (separadas por espaço, opções: a, b, c, d ou e): ").split()
        alunos.append((matricula, respostas))
    return alunos

def calcular_notas(alunos, gabarito):
    notas = []
    for matricula, respostas in alunos:
        nota = sum(1 for resposta, certa in zip(respostas, gabarito) if resposta == certa)
        notas.append((matricula, respostas, nota))
    return notas

def calcular_percentual_aprovacao(notas):
    aprovados = sum(1 for _, _, nota in notas if nota >= 7)
    percentual_aprovacao = (aprovados / len(notas)) * 100
    return percentual_aprovacao

gabarito = ler_gabarito()
alunos = ler_respostas_alunos()

notas = calcular_notas(alunos, gabarito)
percentual_aprovacao = calcular_percentual_aprovacao(notas)

for matricula, respostas, nota in notas:
    print(f"\nMatrícula: {matricula}")
    print(f"Respostas: {' '.join(respostas)}")
    print(f"Nota: {nota}")

print(f"\nPercentual de aprovação: {percentual_aprovacao:.2f}%")