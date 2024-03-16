a, b = map(int, input().split())
#1~a까지의 리스트 만들기
arr = list(range(1, a+1)) #[1, 2, 3, ..., a]
for _ in range(b):
  c, d = map(int, input().split())
  tmp = arr[c-1:d]
  tmp.reverse()
  arr[c-1:d] = tmp

for i in arr:
  print(i, end=' ')