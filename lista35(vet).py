def num_to_list(n):

  return [int(digit) for digit in str(n)][::-1]


def sum_lists(list1, list2):

  max_len = max(len(list1), len(list2))
  result = []
  carry = 0

  for i in range(max_len):
    digit1 = list1[i] if i < len(list1) else 0
    digit2 = list2[i] if i < len(list2) else 0

    total = digit1 + digit2 + carry
    carry = total // 10
    result.append(total % 10)

  if carry:
    result.append(carry)

  return result


def main():

  a = int(input("Digite o primeiro número (menor que 10000): "))
  b = int(input("Digite o segundo número (menor que 10000): "))

  list_a = num_to_list(a)
  list_b = num_to_list(b)

  result = sum_lists(list_a, list_b)

  result_number = ''.join(map(str, result[::-1]))

  print(f"A soma dos números {a} e {b} é: {result_number}")


if __name__ == "__main__":
  main()
