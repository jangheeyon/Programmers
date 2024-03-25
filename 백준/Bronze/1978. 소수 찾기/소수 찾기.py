num = int(input())
arr = list(map(int, input().split()))

for i in range(num):
    if arr[i] == 1:
        num -= 1
    else:
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                num -= 1
                break

print(num)