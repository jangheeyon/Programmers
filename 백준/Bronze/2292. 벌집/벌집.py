# (6*0개) | 1       | 1
# (6*1개) | 2 ~ 7   | 2
# (6*2개) | 8 ~ 19  | 3
# (6*3개) | 9 ~ 37  | 4
# (6*4개) | 10 ~ 61 | 5

n = int(input())
bee_home = 1
cnt = 1

while n > bee_home:
  bee_home += cnt * 6
  cnt += 1

print(cnt)