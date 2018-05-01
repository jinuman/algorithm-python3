# 문자열 반복
# 3 ABC --> AAABBBCCC

tc = int(input())
while tc > 0:
    tc -= 1
    case = input().split()
    result = ""
    for ch in case[1]:
        result += ch * int(case[0])
    print(result)