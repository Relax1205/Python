def main(n):
    dp = [0] * (n + 1)
    dp[0] = 0.07
    if n >= 1:
        dp[1] = 0.24
    for i in range(2, n + 1):
        dp[i] = 65 - (dp[i-1] - dp[i-2] ** 2) / 55
    return dp[n]
