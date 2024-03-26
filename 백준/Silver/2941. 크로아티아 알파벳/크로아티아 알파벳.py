str = input()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#arr을 순회하여 str에 있으면 개수를 셀 수 있게 하나로 바꾸기
for i in arr:
  str = str.replace(i, 'a')

print(len(str))