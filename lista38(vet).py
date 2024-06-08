def insert_and_sort(arr, num):
  arr.append(num)
  arr.sort()


arr = []
print("Digite 10 números:")
for _ in range(10):
  num = int(input())
  insert_and_sort(arr, num)

print("Valores ordenados:", arr)
