def main():
  tam = 15
  vetor = []

  print("Digite 15 números:")
  for i in range(tam):
      numero = int(input())
      vetor.append(numero)

  for i in range(1, tam):
      if vetor[i] == 0 and i > 0:
          vetor[i], vetor[i - 1] = vetor[i - 1], vetor[i]

  print("Vetor compactado:", " ".join(map(str, vetor)))

if __name__ == "__main__":
  main()
