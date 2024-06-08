def main():
    numbers = []

    print("Digite 10 números:")
    for _ in range(10):
        number = float(input())
        numbers.append(number)

    numbers.sort()

    print("Lista ordenada:")
    for num in numbers:
        print(num, end=" ")


if __name__ == "__main__":
    main()
