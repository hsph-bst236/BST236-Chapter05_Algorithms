def min_path_sum_dp(grid: list[list[int]]) -> int:
    """Minimum path sum: Dynamic programming"""
    n, m = len(grid), len(grid[0])
    # Initialize dp table

    # boundary cases
    # State transition: first row

    # State transition: first column


    # State transition: the rest of the rows and columns
    # dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

