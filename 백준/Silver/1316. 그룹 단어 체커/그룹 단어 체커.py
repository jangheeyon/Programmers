cnt = int(input())
answer = cnt

for i in range(cnt):
    str = input()
    for j in range(len(str)-1):
        if str[j]  == str[j+1]:
            continue
        elif str[j] in str[j+1:]:
            answer -= 1
            break
print(answer)