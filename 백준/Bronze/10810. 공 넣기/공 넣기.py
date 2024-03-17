a, b = map(int, input().split())

arr = [0] * (a+1)

for _ in range(b):
  c, d, f = map(int, input().split())
  for i in range(c, d+1):
    arr[i] = f

for j in range(1, a+1):
  print(arr[j], end=' ')
