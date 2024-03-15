a = int(input())
arr = list(map(int, input().split()))
m = max(arr)
for i in range(a):
  arr[i] = float(arr[i]/m * 100)

print(sum(arr)/a)