def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def custom_sort(arr):
    descending_start = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            descending_start = i
            break

    ascending_part = arr[:descending_start]
    descending_part = arr[descending_start:]

    merge_sort(ascending_part)
    merge_sort(descending_part)

    descending_part.reverse()

    arr[:] = ascending_part + descending_part


arr = []
print("Digite 11 números:")
for _ in range(11):
    num = int(input())
    arr.append(num)

custom_sort(arr)

print("Vetor ordenado:", arr)
