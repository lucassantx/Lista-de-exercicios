def main():
    vetor1 = []
    vetor2 = []

    print("Digite 5 valores para o vetor 1:")
    for _ in range(5):
        valor = int(input())
        vetor1.append(valor)

    print("\nDigite 5 valores para o vetor 2:")
    for _ in range(5):
        valor = int(input())
        vetor2.append(valor)

    print("\nsoma dos vetores:")
    for i in range(5):
        soma = vetor1[i] + vetor2[i]
        print(soma)

    print("\nproduto dos vetores:")
    for i in range(5):
        produto = vetor1[i] * vetor2[i]
        print(produto)

    print("\ndiferença dos vetores:")
    difference = sorted(set(vetor1) - set(vetor2))
    for valor in difference:
        print(valor)

    print("\ninterseção dos vetores:")
    intersection = sorted(set(vetor1) & set(vetor2))
    for valor in intersection:
        print(valor)

    print("\nunião dos vetores:")
    uniao = sorted(set(vetor1) | set(vetor2))
    for valor in uniao:
        print(valor)


if __name__ == "__main__":
    main()
