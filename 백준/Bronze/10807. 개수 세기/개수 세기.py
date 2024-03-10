a = int(input())
arr = list(map(int, input().split()))
b = int(input())
result = 0
for i in arr:
  if i == b:
    result+=1
print(result)