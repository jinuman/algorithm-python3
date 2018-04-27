# 피보나치 함수
'''
fibonacci(n)을 호출했을 때 0, 1이 몇번 출력되는지 구하는 문제
'''
dp = [[0 for j in range(2)] for i in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1
tc = int(input())
while tc > 0:
    tc -= 1
    n = int(input())
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[n][0], dp[n][1])

'''
zero = 0
one = 0
def fibonacci(n):
    if n == 0:
        # print(0, "!!")
        global zero
        zero += 1
        return 0
    elif n == 1:
        # print(1, "@@")
        global one
        one += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
tc = int(input())
while tc > 0:
    tc -= 1
    fibonacci(int(input()))
    print(zero, one)
    zero = one = 0
'''