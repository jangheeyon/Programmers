def solution(s):
    min_num = min(map(int, s.split()))
    max_num = max(map(int, s.split()))
    return f'{min_num} {max_num}'