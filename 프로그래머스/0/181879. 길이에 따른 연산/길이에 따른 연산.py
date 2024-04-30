def solution(num_list):
    if len(num_list) >= 11:
        plus = 0
        for i in num_list:
            plus += i
        return plus
    elif len(num_list) <= 10:
        mult = 1
        for i in num_list:
            mult *= i
        return mult
        