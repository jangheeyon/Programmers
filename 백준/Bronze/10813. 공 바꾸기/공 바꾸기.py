a, b = map(int, input().split())
#1~a까지의 리스트 만들기
arr = list(range(1, a+1)) #[1, 2, 3, ..., a]
# b 횟수 만큼 순서 바꿀 것
tmp = 0
for _ in range(b):
  c, d = map(int, input().split())
  tmp = arr[c-1]
  arr[c-1] = arr[d-1]
  arr[d-1] = tmp

for i in arr:
  print(i, end=' ')