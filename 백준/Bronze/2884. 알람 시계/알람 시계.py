h, m = map(int, input().split())
if h == 0 and m < 45:
  h = 24
hh = (((h*60)+m)-45)//60
mm = (((h*60)+m)-45)%60
print(hh, mm, sep=' ')