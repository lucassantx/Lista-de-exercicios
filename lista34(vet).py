def main():
    tam = 10
    vetor = []

    print("Digite 10 numeros diferentes:")
    while len(vetor) < tam:
        numero = int(input())

        if numero in vetor:
            print("Digite um número diferente:")
        else:
            vetor.append(numero)

    print("Vetor:", " ".join(map(str, vetor)))


if __name__ == "__main__":
    main()
