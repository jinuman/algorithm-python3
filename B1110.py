# 더하기 사이클

'''
26 --> 2 + 6 = 8
68 --> 6 + 8 = 14
84 --> 8 + 4 = 12
42 --> 4 + 2 = 6
26 . cycle = 4
'''
n = int(input())
current = n
firstRight = secondRight = 0
sum = 0     # 1의 자리수 + 10의 자리수
cycle = 0
while True:
    if current < 10:
        firstRight = current
        secondRight = current
    else:
        firstRight = current % 10
        sum = current // 10 + firstRight
        if sum < 10:
            secondRight = sum
        else:
            secondRight = sum % 10
    current = firstRight * 10 + secondRight
    cycle += 1
    if n == current:
        break
print(cycle)