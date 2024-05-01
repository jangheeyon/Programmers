def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower() 

    arr1 = []
    arr2 = []
    #두글자씩 끊어서 문자열 검증 후 다중집합으로 만들기
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i]+str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            arr2.append(str2[j]+str2[j+1])

    #교집합, 수 구하기
    intx_arr = []
    arr1_cp = arr1.copy()
    arr2_cp = arr2.copy()
    
    for a1 in arr1:
        if a1 in arr2_cp:
            intx_arr.append(a1)
            arr1_cp.remove(a1)
            arr2_cp.remove(a1)
    intx_cnt = len(intx_arr)

    #합집합, 수 구하기
    all_arr = arr1_cp + arr2_cp + intx_arr
    all_cnt = len(all_arr)

    if all_cnt == 0:
        return 65536
    else:
        return int((intx_cnt / all_cnt) * 65536)