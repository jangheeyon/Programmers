def solution(arr):
    X = []
    for a in arr:
        for _ in range(a):
            X.append(a)
    return X