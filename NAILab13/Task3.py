def knapsack_dp(weights, values, n, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

weights1 = [1, 3, 3, 1]
values1 = [3, 8, 4, 7]
n1 = 4
W1 = 6
print(knapsack_dp(weights1, values1, n1, W1))  # Output: 18

weights2 = [3, 1, 6, 10, 1, 4, 9, 1, 7, 2, 6, 1, 6, 2, 2, 4, 8, 1, 7, 3, 6, 2, 9, 5, 3, 3, 4, 7, 3, 5, 30, 50]
values2 = [7, 4, 9, 18, 9, 15, 4, 2, 6, 13, 18, 12, 12, 16, 19, 19, 10, 16, 14, 3, 14, 4, 15, 7, 5, 10, 10, 13, 19, 9, 8, 5]
n2 = 32
W2 = 75
print(knapsack_dp(weights2, values2, n2, W2))  # Output: 262
