from collections import defaultdict, Counter
def solution(participant, completion):
    answer = ''
    pH = Counter(participant)
    for key in completion:
        pH[key] -= 1
    for key in pH:
        if pH[key] == 1:        
            return key
    return answer
n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n-1):
    b.append(input())
print(solution(a, b))