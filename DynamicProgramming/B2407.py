# 조합
# nCm 을 출력하는 문제
# 5 <= n <= 100, 5 <= m <= 100, m <= n

n, m = map(int, input().split())

dp = [[0 for j in range(101)] for i in range(101)]
dp[1][0] = dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(0, m + 1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][m])
