import os

SOLUTIONS = {
    "404_Introduction_to_DP.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/fibonacci-number/
Problem Name: Introduction to DP (Fibonacci)
Description: Compute Fibonacci number using memoization and space-optimized tabulation.

Folder: Dynamic_Programming
File: 404_Introduction_to_DP.py
\"\"\"

# ============================================
# OPTIMAL APPROACH (Space Optimized)
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(n: int) -> int:
    if n <= 1:
        return n
    prev2, prev = 0, 1
    for _ in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(5) == 5
    assert optimal_solution(10) == 55
    print("Done.")
""",

    "405_Climbing_Stairs.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/climbing-stairs/
Problem Name: Climbing Stairs
Description: Find the number of distinct ways to climb to the top of n stairs.

Folder: Dynamic_Programming
File: 405_Climbing_Stairs.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev = 1, 2
    for _ in range(3, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(3) == 3
    assert optimal_solution(5) == 8
    print("Done.")
""",

    "406_Frog_Jump.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/frog-jump_3621012
Problem Name: Frog Jump
Description: Find minimum energy lost by a frog jumping 1 or 2 steps.

Folder: Dynamic_Programming
File: 406_Frog_Jump.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(heights: list[int]) -> int:
    n = len(heights)
    if n <= 1:
        return 0
    prev2, prev = 0, abs(heights[1] - heights[0])
    for i in range(2, n):
        jump1 = prev + abs(heights[i] - heights[i-1])
        jump2 = prev2 + abs(heights[i] - heights[i-2])
        curr = min(jump1, jump2)
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 20, 30, 10]) == 20
    print("Done.")
""",

    "407_Frog_Jump_with_K_Distance.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/minimal-cost/1
Problem Name: Frog Jump with K Distance
Description: Frog can jump at most K steps. Find minimal energy loss.

Folder: Dynamic_Programming
File: 407_Frog_Jump_with_K_Distance.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(N)
def optimal_solution(heights: list[int], k: int) -> int:
    n = len(heights)
    dp = [0] * n
    for i in range(1, n):
        min_steps = float('inf')
        for j in range(1, min(i, k) + 1):
            min_steps = min(min_steps, dp[i - j] + abs(heights[i] - heights[i - j]))
        dp[i] = min_steps
    return dp[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 30, 40, 50, 20], 3) == 30
    print("Done.")
""",

    "408_Maximum_Sum_of_Non_Adjacent_Elements.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/house-robber/
Problem Name: Maximum Sum of Non-Adjacent Elements
Description: Rob houses without robbing two adjacent houses.

Folder: Dynamic_Programming
File: 408_Maximum_Sum_of_Non_Adjacent_Elements.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    prev2, prev = 0, 0
    for num in nums:
        pick = num + prev2
        non_pick = prev
        curr = max(pick, non_pick)
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 1]) == 4
    assert optimal_solution([2, 7, 9, 3, 1]) == 12
    print("Done.")
""",

    "409_House_Robber.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/house-robber-ii/
Problem Name: House Robber II
Description: Rob houses arranged in a circle. First and last are adjacent.

Folder: Dynamic_Programming
File: 409_House_Robber.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def rob_linear(nums):
    prev2, prev = 0, 0
    for num in nums:
        curr = max(num + prev2, prev)
        prev2 = prev
        prev = curr
    return prev

def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([2, 3, 2]) == 3
    assert optimal_solution([1, 2, 3, 1]) == 4
    print("Done.")
""",

    "410_Ninjas_training.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/ninja-s-training_3621003
Problem Name: Ninja's Training
Description: Ninja performs 1 of 3 activities daily. Cannot perform same activity on consecutive days. Maximize merit points.

Folder: Dynamic_Programming
File: 410_Ninjas_training.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * 4 * 3) = O(N)
# Space Complexity: O(1)
def optimal_solution(points: list[list[int]]) -> int:
    prev = [0] * 4
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))
    
    n = len(points)
    for day in range(1, n):
        temp = [0] * 4
        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if task != last:
                    pts = points[day][task] + prev[task]
                    temp[last] = max(temp[last], pts)
        prev = temp
    return prev[3]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    points = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
    assert optimal_solution(points) == 11
    print("Done.")
""",

    "411_Grid_Unique_Paths_DP_on_Grids_DP8.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/unique-paths/
Problem Name: Unique Paths
Description: Count unique paths from top-left to bottom-right in m x n grid.

Folder: Dynamic_Programming
File: 411_Grid_Unique_Paths_DP_on_Grids_DP8.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(M * N)
# Space Complexity: O(N)
def optimal_solution(m: int, n: int) -> int:
    prev = [1] * n
    for i in range(1, m):
        curr = [1] * n
        for j in range(1, n):
            curr[j] = curr[j - 1] + prev[j]
        prev = curr
    return prev[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(3, 7) == 28
    assert optimal_solution(3, 2) == 3
    print("Done.")
""",

    "412_Unique_paths_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/unique-paths-ii/
Problem Name: Unique Paths II
Description: Unique paths with obstacles (denoted as 1).

Folder: Dynamic_Programming
File: 412_Unique_paths_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(M * N)
# Space Complexity: O(N)
def optimal_solution(obstacleGrid: list[list[int]]) -> int:
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1
    
    for r in range(m):
        for c in range(n):
            if obstacleGrid[r][c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert optimal_solution(grid) == 2
    print("Done.")
""",

    "413_Minimum_Falling_Path_Sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/minimum-falling-path-sum/
Problem Name: Minimum Falling Path Sum
Description: Minimum sum of falling path from top row to bottom row.

Folder: Dynamic_Programming
File: 413_Minimum_Falling_Path_Sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(matrix: list[list[int]]) -> int:
    n = len(matrix)
    prev = list(matrix[0])
    
    for r in range(1, n):
        curr = [0] * n
        for c in range(n):
            val = matrix[r][c]
            mid = prev[c]
            left = prev[c - 1] if c > 0 else float('inf')
            right = prev[c + 1] if c < n - 1 else float('inf')
            curr[c] = val + min(mid, left, right)
        prev = curr
    return min(prev)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    assert optimal_solution(matrix) == 13
    print("Done.")
""",

    "414_Triangle.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/triangle/
Problem Name: Triangle Minimum Path Sum
Description: Find minimum path sum from top to bottom of triangle grid.

Folder: Dynamic_Programming
File: 414_Triangle.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N) bottom-up
def optimal_solution(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = list(triangle[-1])
    for r in range(n - 2, -1, -1):
        for c in range(r + 1):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
    return dp[0]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    assert optimal_solution(triangle) == 11
    print("Done.")
""",

    "415_Ninja_and_his_Friends.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/cherry-pickup-ii/
Problem Name: Cherry Pickup II (Ninja and his Friends)
Description: 3D DP. Two robots starting at (0,0) and (0, C-1) picking cherries on grid.

Folder: Dynamic_Programming
File: 415_Ninja_and_his_Friends.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C * C * 9)
# Space Complexity: O(C * C)
def optimal_solution(grid: list[list[int]]) -> int:
    r, c = len(grid), len(grid[0])
    dp = [[-float('inf')] * c for _ in range(c)]
    dp[0][c - 1] = grid[0][0] + grid[0][c - 1] if c > 1 else grid[0][0]
    
    for row in range(1, r):
        next_dp = [[-float('inf')] * c for _ in range(c)]
        for c1 in range(c):
            for c2 in range(c):
                # Rob1 is at c1, Rob2 is at c2
                cherry = grid[row][c1] + (grid[row][c2] if c1 != c2 else 0)
                max_prev = -float('inf')
                for dc1 in (-1, 0, 1):
                    for dc2 in (-1, 0, 1):
                        pc1, pc2 = c1 + dc1, c2 + dc2
                        if 0 <= pc1 < c and 0 <= pc2 < c:
                            max_prev = max(max_prev, dp[pc1][pc2])
                next_dp[c1][c2] = max_prev + cherry
        dp = next_dp
        
    return max(max(row) for row in dp)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    assert optimal_solution(grid) == 24
    print("Done.")
""",

    "416_Subset_sum_equal_to_target_DP_14.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555635/1
Problem Name: Subset Sum Equal to Target
Description: Check if subset exists with sum equal to target.

Folder: Dynamic_Programming
File: 416_Subset_sum_equal_to_target_DP_14.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
def optimal_solution(arr: list[int], target: int) -> bool:
    dp = [False] * (target + 1)
    dp[0] = True
    if arr[0] <= target:
        dp[arr[0]] = True
        
    for i in range(1, len(arr)):
        next_dp = [False] * (target + 1)
        next_dp[0] = True
        for t in range(1, target + 1):
            non_pick = dp[t]
            pick = dp[t - arr[i]] if t >= arr[i] else False
            next_dp[t] = pick or non_pick
        dp = next_dp
    return dp[target]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 4], 6) == True
    assert optimal_solution([1, 2, 3, 4], 11) == False
    print("Done.")
""",

    "417_Partition_equal_subset_sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/partition-equal-subset-sum/
Problem Name: Partition Equal Subset Sum
Description: Check if array can be partitioned into two subsets with equal sum.

Folder: Dynamic_Programming
File: 417_Partition_equal_subset_sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * Sum/2)
# Space Complexity: O(Sum/2)
def optimal_solution(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    if nums[0] <= target:
        dp[nums[0]] = True
        
    for i in range(1, len(nums)):
        next_dp = [False] * (target + 1)
        next_dp[0] = True
        for t in range(1, target + 1):
            non_pick = dp[t]
            pick = dp[t - nums[i]] if t >= nums[i] else False
            next_dp[t] = pick or non_pick
        dp = next_dp
    return dp[target]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 5, 11, 5]) == True
    assert optimal_solution([1, 2, 3, 5]) == False
    print("Done.")
""",

    "418_Partition_a_set_into_two_subsets_with_minimum_absolute_sum_difference.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/last-stone-weight-ii/
Problem Name: Partition set with minimum absolute sum difference
Description: Partition set into two subsets with minimum absolute sum difference.

Folder: Dynamic_Programming
File: 418_Partition_a_set_into_two_subsets_with_minimum_absolute_sum_difference.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * TotalSum)
# Space Complexity: O(TotalSum)
def optimal_solution(nums: list[int]) -> int:
    total_sum = sum(nums)
    target = total_sum // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    if nums[0] <= target:
        dp[nums[0]] = True
        
    for i in range(1, len(nums)):
        for t in range(target, nums[i] - 1, -1):
            dp[t] = dp[t] or dp[t - nums[i]]
            
    # Find maximum sum s1 <= target that is achievable
    s1 = 0
    for t in range(target, -1, -1):
        if dp[t]:
            s1 = t
            break
            
    s2 = total_sum - s1
    return abs(s1 - s2)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 6, 11, 5]) == 1 # subsets {1, 5, 6}=12 and {11}=11
    print("Done.")
""",

    "419_Count_subsets_with_sum_K.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
Problem Name: Count Subsets with Sum K
Description: Count number of subsets that sum to K.

Folder: Dynamic_Programming
File: 419_Count_subsets_with_sum_K.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(K)
def optimal_solution(arr: list[int], k: int) -> int:
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for num in arr:
        for t in range(k, num - 1, -1):
            dp[t] += dp[t - num]
    return dp[k]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 2, 3], 3) == 3
    print("Done.")
""",

    "420_Count_partitions_with_given_difference.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/partitions-with-given-difference_3751628
Problem Name: Partitions with Given Difference
Description: Count partitions s1 and s2 such that s1 - s2 = D and s1 >= s2.

Folder: Dynamic_Programming
File: 420_Count_partitions_with_given_difference.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: s1 + s2 = total, s1 - s2 = diff => 2*s1 = total + diff => s1 = (total + diff) / 2.
# Target is s1.
# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
def optimal_solution(arr: list[int], diff: int) -> int:
    total = sum(arr)
    if (total + diff) % 2 != 0 or total < diff:
        return 0
    target = (total + diff) // 2
    
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in arr:
        for t in range(target, num - 1, -1):
            dp[t] += dp[t - num]
    return dp[target]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([5, 2, 6, 4], 3) == 1
    print("Done.")
""",

    "421_Assign_Cookies_DP.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/assign-cookies/
Problem Name: Assign Cookies (Greedy/DP)
Description: Maximize content children given greed factor and cookie sizes.

Folder: Dynamic_Programming
File: 421_Assign_Cookies_DP.py
\"\"\"

# ============================================
# OPTIMAL APPROACH (Greedy)
# ============================================
# Time Complexity: O(N log N + M log M)
# Space Complexity: O(1)
def optimal_solution(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3], [1, 1]) == 1
    assert optimal_solution([1, 2], [1, 2, 3]) == 2
    print("Done.")
""",

    "422_Minimum_Coins_DP_20.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/coin-change/
Problem Name: Coin Change (Minimum Coins)
Description: Fewest number of coins needed to make up amount.

Folder: Dynamic_Programming
File: 422_Minimum_Coins_DP_20.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(Coins * Amount)
# Space Complexity: O(Amount)
def optimal_solution(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for t in range(coin, amount + 1):
            dp[t] = min(dp[t], 1 + dp[t - coin])
    return dp[amount] if dp[amount] != float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 5], 11) == 3
    assert optimal_solution([2], 3) == -1
    print("Done.")
""",

    "423_Target_sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/target-sum/
Problem Name: Target Sum
Description: Assign '+' and '-' to elements to sum to target.

Folder: Dynamic_Programming
File: 423_Target_sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Equivalent to Count Partitions with Given Difference target = (sum + diff) / 2.
# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
def optimal_solution(nums: list[int], target: int) -> int:
    total = sum(nums)
    if (total + target) % 2 != 0 or total < abs(target):
        return 0
    t = (total + target) // 2
    
    dp = [0] * (t + 1)
    dp[0] = 1
    for num in nums:
        for val in range(t, num - 1, -1):
            dp[val] += dp[val - num]
    return dp[t]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 1, 1, 1, 1], 3) == 5
    print("Done.")
""",

    "424_Coin_Change_2_DP_22.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/coin-change-ii/
Problem Name: Coin Change 2
Description: Number of combinations that make up amount. Unlimited reuse.

Folder: Dynamic_Programming
File: 424_Coin_Change_2_DP_22.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(Coins * Amount)
# Space Complexity: O(Amount)
def optimal_solution(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for t in range(coin, amount + 1):
            dp[t] += dp[t - coin]
    return dp[amount]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(5, [1, 2, 5]) == 4
    print("Done.")
""",

    "425_Unbounded_knapsack.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/unbounded-knapsack5444/1
Problem Name: Unbounded Knapsack
Description: Pick items to maximize profit within capacity. Unlimited repetitions.

Folder: Dynamic_Programming
File: 425_Unbounded_knapsack.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * W)
# Space Complexity: O(W)
def optimal_solution(val: list[int], wt: list[int], w: int) -> int:
    dp = [0] * (w + 1)
    for i in range(len(val)):
        for t in range(wt[i], w + 1):
            dp[t] = max(dp[t], val[i] + dp[t - wt[i]])
    return dp[w]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 1], [2, 1], 3) == 3
    print("Done.")
""",

    "426_Rod_Cutting_Problem_DP_24.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/rod-cutting0840/1
Problem Name: Rod Cutting
Description: Cut rod of length N to maximize price. Length price list given.

Folder: Dynamic_Programming
File: 426_Rod_Cutting_Problem_DP_24.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Unbounded knapsack setup where wt[i] = i + 1, capacity = N.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(price: list[int], n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(n):
        wt = i + 1
        val = price[i]
        for t in range(wt, n + 1):
            dp[t] = max(dp[t], val + dp[t - wt])
    return dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 5, 8, 9, 10, 17, 17, 20], 8) == 22
    print("Done.")
""",

    "427_Longest_common_subsequence.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/longest-common-subsequence/
Problem Name: Longest Common Subsequence
Description: Length of longest common subsequence of two strings.

Folder: Dynamic_Programming
File: 427_Longest_common_subsequence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M) space optimized
def optimal_solution(text1: str, text2: str) -> int:
    m = len(text2)
    dp = [0] * (m + 1)
    
    for c1 in text1:
        next_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            if c1 == text2[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("abcde", "ace") == 3
    print("Done.")
""",

    "428_Print_Longest_Common_Subsequence_DP_26.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1
Problem Name: Print Longest Common Subsequence
Description: Return the actual string representing the LCS.

Folder: Dynamic_Programming
File: 428_Print_Longest_Common_Subsequence_DP_26.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
def optimal_solution(text1: str, text2: str) -> str:
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # Backtrack
    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs[::-1])

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("abcde", "ace") == "ace"
    print("Done.")
""",

    "429_Longest_common_substring.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
Problem Name: Longest Common Substring
Description: Find length of longest common substring of two strings.

Folder: Dynamic_Programming
File: 429_Longest_common_substring.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(s1: str, s2: str) -> int:
    m = len(s2)
    dp = [0] * (m + 1)
    max_len = 0
    for char in s1:
        next_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            if char == s2[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
                max_len = max(max_len, next_dp[j])
        dp = next_dp
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("ABCDGH", "ACDGHR") == 4 # "CDGH"
    print("Done.")
""",

    "430_Longest_palindromic_subsequence.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/longest-palindromic-subsequence/
Problem Name: Longest Palindromic Subsequence
Description: Find length of longest palindromic subsequence of string.

Folder: Dynamic_Programming
File: 430_Longest_palindromic_subsequence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: LCS of string s and its reverse s[::-1].
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(s: str) -> int:
    s_rev = s[::-1]
    n = len(s)
    dp = [0] * (n + 1)
    for char in s:
        next_dp = [0] * (n + 1)
        for j in range(1, n + 1):
            if char == s_rev[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("bbbab") == 4
    print("Done.")
""",

    "431_Minimum_insertions_to_make_string_palindrome_DP_29.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
Problem Name: Minimum Insertions to Make String Palindrome
Description: Return minimum insertions to make string a palindrome.

Folder: Dynamic_Programming
File: 431_Minimum_insertions_to_make_string_palindrome_DP_29.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Result is len(s) - Longest Palindromic Subsequence(s).
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(s: str) -> int:
    n = len(s)
    rev = s[::-1]
    dp = [0] * (n + 1)
    for char in s:
        next_dp = [0] * (n + 1)
        for j in range(1, n + 1):
            if char == rev[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return n - dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("zzazz") == 0
    assert optimal_solution("mbadm") == 2
    print("Done.")
""",

    "432_Minimum_insertions_or_deletions_to_convert_string_A_to_B.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/delete-operation-for-two-strings/
Problem Name: Delete Operation for Two Strings (Min Insert/Delete)
Description: Find minimum steps to make two strings identical (insert or delete).

Folder: Dynamic_Programming
File: 432_Minimum_insertions_or_deletions_to_convert_string_A_to_B.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Result is len(s1) + len(s2) - 2 * LCS(s1, s2).
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    dp = [0] * (m + 1)
    for char in word1:
        next_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            if char == word2[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return n + m - 2 * dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("sea", "eat") == 2
    print("Done.")
""",

    "433_Shortest_common_supersequence.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/shortest-common-supersequence/
Problem Name: Shortest Common Supersequence
Description: Find shortest supersequence that contains both strings as subsequences.

Folder: Dynamic_Programming
File: 433_Shortest_common_supersequence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(N * M) for backtracking matrix
def optimal_solution(str1: str, str2: str) -> str:
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    i, j = n, m
    ans = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            ans.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            ans.append(str1[i - 1])
            i -= 1
        else:
            ans.append(str2[j - 1])
            j -= 1
            
    while i > 0:
        ans.append(str1[i - 1])
        i -= 1
    while j > 0:
        ans.append(str2[j - 1])
        j -= 1
        
    return "".join(ans[::-1])

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("abac", "cab") == "cabac"
    print("Done.")
""",

    "434_Distinct_subsequences.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/distinct-subsequences/
Problem Name: Distinct Subsequences
Description: Count number of times string T appears as subsequence in string S.

Folder: Dynamic_Programming
File: 434_Distinct_subsequences.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(s: str, t: str) -> int:
    m = len(t)
    dp = [0] * (m + 1)
    dp[0] = 1 # Empty string t is always a subsequence
    
    for char in s:
        # Backwards iteration to use single row
        for j in range(m, 0, -1):
            if char == t[j - 1]:
                dp[j] = dp[j] + dp[j - 1]
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("rabbbit", "rabbit") == 3
    print("Done.")
""",

    "435_Edit_distance.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/edit-distance/
Problem Name: Edit Distance
Description: Find minimum operations (insert, delete, replace) to convert word1 to word2.

Folder: Dynamic_Programming
File: 435_Edit_distance.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(word1: str, word2: str) -> int:
    m = len(word2)
    dp = list(range(m + 1))
    
    for char in word1:
        next_dp = [0] * (m + 1)
        next_dp[0] = dp[0] + 1
        for j in range(1, m + 1):
            if char == word2[j - 1]:
                next_dp[j] = dp[j - 1]
            else:
                next_dp[j] = 1 + min(dp[j], next_dp[j - 1], dp[j - 1])
        dp = next_dp
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("horse", "ros") == 3
    print("Done.")
""",

    "436_Wildcard_matching.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/wildcard-matching/
Problem Name: Wildcard Matching
Description: Match string s with pattern p supporting '?' and '*'.

Folder: Dynamic_Programming
File: 436_Wildcard_matching.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(s: str, p: str) -> bool:
    m = len(p)
    dp = [False] * (m + 1)
    dp[0] = True
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[j] = dp[j - 1]
            
    for char in s:
        next_dp = [False] * (m + 1)
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                next_dp[j] = next_dp[j - 1] or dp[j]
            elif p[j - 1] == '?' or char == p[j - 1]:
                next_dp[j] = dp[j - 1]
        dp = next_dp
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("aa", "*") == True
    assert optimal_solution("cb", "?a") == False
    print("Done.")
""",

    "437_Best_time_to_buy_and_sell_stock.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem Name: Best Time to Buy and Sell Stock I
Description: Find maximum profit making at most 1 transaction.

Folder: Dynamic_Programming
File: 437_Best_time_to_buy_and_sell_stock.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([7, 1, 5, 3, 6, 4]) == 5
    print("Done.")
""",

    "438_Best_time_to_buy_and_sell_stock_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Problem Name: Best Time to Buy and Sell Stock II
Description: Maximize profit making unlimited transactions.

Folder: Dynamic_Programming
File: 438_Best_time_to_buy_and_sell_stock_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([7, 1, 5, 3, 6, 4]) == 7
    print("Done.")
""",

    "439_Best_time_to_buy_and_sell_stock_III.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Problem Name: Best Time to Buy and Sell Stock III
Description: Maximize profit making at most 2 transactions.

Folder: Dynamic_Programming
File: 439_Best_time_to_buy_and_sell_stock_III.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    # Track min price and max profit for transaction 1 and 2
    cost1, cost2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0
    for price in prices:
        cost1 = min(cost1, price)
        profit1 = max(profit1, price - cost1)
        cost2 = min(cost2, price - profit1) # reinvest profit1
        profit2 = max(profit2, price - cost2)
    return profit2

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 3, 5, 0, 0, 8, 2, 5]) == 19
    print("Done.")
""",

    "440_Best_time_to_buy_and_sell_stock_IV.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Problem Name: Best Time to Buy and Sell Stock IV
Description: Maximize profit making at most K transactions.

Folder: Dynamic_Programming
File: 440_Best_time_to_buy_and_sell_stock_IV.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(K)
def optimal_solution(k: int, prices: list[int]) -> int:
    if not prices:
        return 0
    costs = [float('inf')] * k
    profits = [0] * k
    for price in prices:
        for i in range(k):
            prev_profit = profits[i - 1] if i > 0 else 0
            costs[i] = min(costs[i], price - prev_profit)
            profits[i] = max(profits[i], price - costs[i])
    return profits[-1] if k > 0 else 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(2, [3, 2, 6, 5, 0, 3]) == 7
    print("Done.")
""",

    "441_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Problem Name: Best Time to Buy and Sell Stock with Cooldown
Description: Maximize profit with cooldown of 1 day after sell.

Folder: Dynamic_Programming
File: 441_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    if not prices:
        return 0
    # State tracking: buy[i], sell[i], cooldown[i]
    # buy: max profit ending with buy (or hold buy)
    # sell: max profit ending with sell
    # cooldown: max profit in cooldown
    buy = -prices[0]
    sell = 0
    cooldown = 0
    for price in prices[1:]:
        prev_sell = sell
        sell = max(sell, buy + price)
        buy = max(buy, cooldown - price)
        cooldown = max(cooldown, prev_sell)
    return sell

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 0, 2]) == 3
    print("Done.")
""",

    "442_Best_time_to_buy_and_sell_stock_with_transaction_fees.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Problem Name: Best Time to Buy and Sell Stock with Transaction Fee
Description: Maximize profit with transaction fee per transaction.

Folder: Dynamic_Programming
File: 442_Best_time_to_buy_and_sell_stock_with_transaction_fees.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int], fee: int) -> int:
    # hold: max profit holding stock
    # free: max profit not holding stock
    hold = -prices[0]
    free = 0
    for price in prices[1:]:
        free = max(free, hold + price - fee)
        hold = max(hold, free - price)
    return free

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 3, 2, 8, 4, 9], 2) == 8
    print("Done.")
""",

    "443_Longest_Increasing_Subsequence.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/longest-increasing-subsequence/
Problem Name: Longest Increasing Subsequence
Description: Length of longest strictly increasing subsequence.

Folder: Dynamic_Programming
File: 443_Longest_Increasing_Subsequence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("Done.")
""",

    "444_Print_Longest_Increasing_Subsequence.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1
Problem Name: Print Longest Increasing Subsequence
Description: Return actual LIS path.

Folder: Dynamic_Programming
File: 444_Print_Longest_Increasing_Subsequence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> list[int]:
    n = len(nums)
    dp = [1] * n
    hash_prev = list(range(n))
    max_len = 1
    last_idx = 0
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                hash_prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            last_idx = i
            
    # Backtrack
    lis = []
    curr = last_idx
    while hash_prev[curr] != curr:
        lis.append(nums[curr])
        curr = hash_prev[curr]
    lis.append(nums[curr])
    return lis[::-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == [2, 3, 7, 18] or optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == [2, 5, 7, 18]
    print("Done.")
""",

    "445_Longest_Increasing_Subsequence_DP_43.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/longest-increasing-subsequence/
Problem Name: Longest Increasing Subsequence (Binary Search)
Description: Compute LIS in O(N log N) time using binary search (piles / patience sorting).

Folder: Dynamic_Programming
File: 445_Longest_Increasing_Subsequence_DP_43.py
\"\"\"

import bisect

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    sub = []
    for num in nums:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    return len(sub)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("Done.")
""",

    "446_Largest_Divisible_Subset.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/largest-divisible-subset/
Problem Name: Largest Divisible Subset
Description: Find largest subset where every pair satisfies s[i] % s[j] == 0 or vice versa.

Folder: Dynamic_Programming
File: 446_Largest_Divisible_Subset.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort nums first. Standard LIS format where condition is nums[i] % nums[j] == 0.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> list[int]:
    if not nums:
        return []
    nums.sort()
    n = len(nums)
    dp = [1] * n
    parent = list(range(n))
    max_len = 1
    last_idx = 0
    
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            last_idx = i
            
    res = []
    curr = last_idx
    while parent[curr] != curr:
        res.append(nums[curr])
        curr = parent[curr]
    res.append(nums[curr])
    return res[::-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3]) == [1, 2] or optimal_solution([1, 2, 3]) == [1, 3]
    print("Done.")
""",

    "447_Longest_String_Chain.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/longest-string-chain/
Problem Name: Longest String Chain
Description: Longest chain of strings where words[i] can be formed by adding 1 char to words[i-1].

Folder: Dynamic_Programming
File: 447_Longest_String_Chain.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort words by length. Use map dp[word] representing chain length ending at word.
# Time Complexity: O(N * L^2) where L is max word length
# Space Complexity: O(N)
def optimal_solution(words: list[str]) -> int:
    words.sort(key=len)
    dp = {}
    max_chain = 1
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_chain = max(max_chain, dp[word])
    return max_chain

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(["a","b","ba","bca","bda","bdca"]) == 4
    print("Done.")
""",

    "448_Longest_Bitonic_Subsequence.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1
Problem Name: Longest Bitonic Subsequence
Description: Longest bitonic subsequence (strictly increasing then strictly decreasing).

Folder: Dynamic_Programming
File: 448_Longest_Bitonic_Subsequence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Find LIS from front (dp1) and LIS from back (dp2).
# Maximize (dp1[i] + dp2[i] - 1).
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp1 = [1] * n # increasing
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
                
    dp2 = [1] * n # decreasing
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
                
    max_len = 0
    for i in range(n):
        if dp1[i] > 1 and dp2[i] > 1: # Strict bitonic requires both increasing and decreasing parts
            max_len = max(max_len, dp1[i] + dp2[i] - 1)
    # If no bitonic found, return max LIS (or 0 per GFG strict testcases)
    return max_len if max_len > 0 else max(max(dp1), max(dp2))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 5, 3, 2]) == 5
    print("Done.")
""",

    "449_Number_of_Longest_Increasing_Subsequences.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
Problem Name: Number of Longest Increasing Subsequences
Description: Count number of LIS possible.

Folder: Dynamic_Programming
File: 449_Number_of_Longest_Increasing_Subsequences.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep dp[i] representing length of LIS ending at i, and count[i] representing total ways.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    count = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]
                    
    max_len = max(dp)
    ans = 0
    for i in range(n):
        if dp[i] == max_len:
            ans += count[i]
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 3, 5, 4, 7]) == 2
    print("Done.")
""",

    "450_Matrix_chain_multiplication.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
Problem Name: Matrix Chain Multiplication (MCM)
Description: Find minimal cost to multiply matrices.

Folder: Dynamic_Programming
File: 450_Matrix_chain_multiplication.py
\"\"\"

# ============================================
# OPTIMAL APPROACH (Memoized Top-Down)
# ============================================
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(arr: list[int]) -> int:
    n = len(arr)
    memo = {}
    
    def solve(i, j):
        if i == j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
            
        min_cost = float('inf')
        for k in range(i, j):
            cost = solve(i, k) + solve(k + 1, j) + arr[i-1] * arr[k] * arr[j]
            min_cost = min(min_cost, cost)
            
        memo[(i, j)] = min_cost
        return min_cost

    return solve(1, n - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([40, 20, 30, 10, 30]) == 26000
    print("Done.")
""",

    "451_Matrix_Chain_Multiplication_Bottom_UpDP_49.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
Problem Name: Matrix Chain Multiplication (Bottom-Up)
Description: Tabulation approach of MCM.

Folder: Dynamic_Programming
File: 451_Matrix_Chain_Multiplication_Bottom_UpDP_49.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(arr: list[int]) -> int:
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    # l is chain length
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
                
    return dp[1][n - 1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([40, 20, 30, 10, 30]) == 26000
    print("Done.")
""",

    "452_Minimum_cost_to_cut_the_stick.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
Problem Name: Minimum Cost to Cut a Stick
Description: Find minimal cost to make all cuts on a stick of length N.

Folder: Dynamic_Programming
File: 452_Minimum_cost_to_cut_the_stick.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort cuts. Append 0 and N to cuts array. Partition space.
# Time Complexity: O(M^3) where M is cuts length
# Space Complexity: O(M^2)
def optimal_solution(n: int, cuts: list[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)
    dp = [[0] * m for _ in range(m)]
    
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
                
    return dp[0][m - 1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(7, [1, 3, 4, 5]) == 16
    print("Done.")
""",

    "453_Burst_balloons.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/burst-balloons/
Problem Name: Burst Balloons
Description: Burst balloons to maximize coins collected.

Folder: Dynamic_Programming
File: 453_Burst_balloons.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: MCM layout. Define subproblem as last balloon to burst in range (i, j).
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(nums: list[int]) -> int:
    arr = [1] + nums + [1]
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    for l in range(1, n - 1):
        for i in range(1, n - l):
            j = i + l - 1
            for k in range(i, j + 1):
                coins = arr[i - 1] * arr[k] * arr[j + 1]
                coins += dp[i][k - 1] + dp[k + 1][j]
                dp[i][j] = max(dp[i][j], coins)
                
    return dp[1][n - 2]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 1, 5, 8]) == 167
    print("Done.")
""",

    "454_Different_Ways_to_Evaluate_a_Boolean_Expression.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1
Problem Name: Boolean Parenthesization
Description: Count ways to parenthesize expression to evaluate to True.

Folder: Dynamic_Programming
File: 454_Different_Ways_to_Evaluate_a_Boolean_Expression.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(s: str) -> int:
    MOD = 1003
    n = len(s)
    memo = {}
    
    def solve(i, j, is_true):
        if i > j:
            return 0
        if i == j:
            if is_true:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0
                
        key = (i, j, is_true)
        if key in memo:
            return memo[key]
            
        ways = 0
        for k in range(i + 1, j, 2):
            lt = solve(i, k - 1, True)
            lf = solve(i, k - 1, False)
            rt = solve(k + 1, j, True)
            rf = solve(k + 1, j, False)
            
            op = s[k]
            if op == '&':
                if is_true:
                    ways += lt * rt
                else:
                    ways += lf * rt + lt * rf + lf * rf
            elif op == '|':
                if is_true:
                    ways += lt * rt + lf * rt + lt * rf
                else:
                    ways += lf * rf
            elif op == '^':
                if is_true:
                    ways += lt * rf + lf * rt
                else:
                    ways += lt * rt + lf * rf
                    
        memo[key] = ways % MOD
        return memo[key]

    return solve(0, n - 1, True)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("T|F^F") == 2
    print("Done.")
""",

    "455_Palindrome_partitioning_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/palindrome-partitioning-ii/
Problem Name: Palindrome Partitioning II
Description: Find minimal cuts needed for palindrome partitioning of a string.

Folder: Dynamic_Programming
File: 455_Palindrome_partitioning_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
def optimal_solution(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                is_pal[i][j] = (s[i] == s[j])
            else:
                is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
                
    cuts = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            cuts[i] = 0
        else:
            min_cut = float('inf')
            for j in range(i):
                if is_pal[j + 1][i]:
                    min_cut = min(min_cut, cuts[j] + 1)
            cuts[i] = min_cut
    return cuts[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("aab") == 1
    print("Done.")
""",

    "456_Partition_Array_for_Maximum_Sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/partition-array-for-maximum-sum/
Problem Name: Partition Array for Maximum Sum
Description: Partition array into subarrays of at most length k. Maximize sum of elements.

Folder: Dynamic_Programming
File: 456_Partition_Array_for_Maximum_Sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(N)
def optimal_solution(arr: list[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        curr_max = 0
        for j in range(1, min(i, k) + 1):
            curr_max = max(curr_max, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + curr_max * j)
            
    return dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 15, 7, 9, 2, 5, 10], 3) == 84
    print("Done.")
""",

    "457_Maximum_Rectangle_Area_with_all_1sDP_55.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/maximal-rectangle/
Problem Name: Maximal Rectangle Area with all 1s
Description: Find largest rectangle area containing only 1s in a 2D matrix.

Folder: Dynamic_Programming
File: 457_Maximum_Rectangle_Area_with_all_1sDP_55.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: For each row, construct heights array (histogram). Find max area in histogram.
# Time Complexity: O(R * C)
# Space Complexity: O(C)
def max_histogram_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else (i - stack[-1] - 1)
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area

def optimal_solution(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    max_rect = 0
    for row in matrix:
        for c in range(cols):
            heights[c] = heights[c] + 1 if row[c] == "1" else 0
        max_rect = max(max_rect, max_histogram_area(heights))
    return max_rect

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert optimal_solution(matrix) == 6
    print("Done.")
""",

    "458_Count_Square_Submatrices_with_All_OnesDP_56.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
Problem Name: Count Square Submatrices with All Ones
Description: Count total square submatrices that have all ones.

Folder: Dynamic_Programming
File: 458_Count_Square_Submatrices_with_All_OnesDP_56.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: dp[r][c] represents size of largest square ending at (r, c).
# dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) if matrix[r][c] == 1.
# Total count is sum of all values in dp table.
# Time Complexity: O(R * C)
# Space Complexity: O(C) space optimized
def optimal_solution(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * cols
    total_squares = 0
    prev_diag = 0 # stores dp[r-1][c-1]
    
    for r in range(rows):
        for c in range(cols):
            temp = dp[c]
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    dp[c] = 1
                else:
                    dp[c] = 1 + min(dp[c], dp[c - 1], prev_diag)
                total_squares += dp[c]
            else:
                dp[c] = 0
            prev_diag = temp
    return total_squares

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
    assert optimal_solution(matrix) == 15
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Dynamic_Programming", "Code")
    os.makedirs(target_dir, exist_ok=True)
    
    # Remove README.py if it exists
    readme_py = os.path.join(target_dir, "README.py")
    if os.path.exists(readme_py):
        os.remove(readme_py)
        print("Removed temporary README.py")
        
    for filename, code in SOLUTIONS.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Populated {filename}")
        
    print("All DP code solutions populated successfully!")

if __name__ == "__main__":
    main()
