str = input().upper()

word = list(set(str))

arr = []
for i in word:
  cnt = str.count(i)
  arr.append(cnt)

if arr.count(max(arr)) > 1 :
  print('?')
else:
  idx = arr.index(max(arr))
  print(word[idx])