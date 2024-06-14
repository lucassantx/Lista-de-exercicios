def ler_matriz_respostas():
    matriz = []
    for i in range(5):
        linha = input(f"Digite as respostas do aluno {i + 1} (separadas por espaço): ").split()
        matriz.append(linha)
    return matriz

def ler_gabarito():
    gabarito = input("Digite o gabarito (10 respostas separadas por espaço): ").split()
    return gabarito

def calcular_pontuacoes(matriz, gabarito):
    resultado = []
    for aluno in matriz:
        pontuacao = sum(1 for resposta, certa in zip(aluno, gabarito) if resposta == certa)
        resultado.append(pontuacao)
    return resultado

matriz_respostas = ler_matriz_respostas()
gabarito = ler_gabarito()

resultado = calcular_pontuacoes(matriz_respostas, gabarito)

for i, pontuacao in enumerate(resultado):
    print(f"Pontuação do aluno {i + 1}: {pontuacao}")