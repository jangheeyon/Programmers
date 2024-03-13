a, b = map(int, input().split())
ra = int(str(a)[::-1])
rb = int(str(b)[::-1])
if ra > rb:
  print(ra)
else:
  print(rb)