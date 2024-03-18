arr = [1, 1, 2, 2, 2, 8]

arr2 = list(map(int, input().split()))

arr3 = [0] * 6

for i in range(6):
  arr3[i] = arr[i] - arr2[i]

for j in arr3:
  print(j, end=' ')
