def m10(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1
    return contador

def matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

matriz = matriz()
mais10 = m10(matriz)
print(f"A matriz possui {mais10} valores maiores que 10.")