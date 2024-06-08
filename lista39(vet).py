def generate_pascal_triangle(n):
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))


def main():
    n = int(input("Digite o número de linhas do Triângulo de Pascal: "))
    pascal_triangle = generate_pascal_triangle(n)
    print("Triângulo de Pascal com", n, "linhas:")
    print_pascal_triangle(pascal_triangle)


if __name__ == "__main__":
    main()
