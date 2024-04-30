def solution(n, lost, reserve):
    #여분이 있는데 도난 당한 사람은 빼기
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    #여분_set을 순회해서 앞, 뒤 번호를 찾고, 해당하는 값이 도난에 있으면 도난에서 빼기(빌려줌)
    for reserve in reserve_set:
        bf = reserve - 1
        af = reserve + 1
        if bf in lost_set:
            lost_set.remove(bf)
        elif af in lost_set:
            lost_set.remove(af)
    
    #도난_set에는 빌리지 못한 도난 당한 사람만 남음
    lost_people = len(lost_set)

    #전체 학생 수에서 빌리지 못한 도난 당한 사람을 빼면 모두 체육복을 가진 사람
    return n - lost_people
