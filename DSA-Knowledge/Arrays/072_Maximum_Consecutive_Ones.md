# Maximum Consecutive Ones

## Difficulty
Easy

---

## Pattern
Iterative / Running Counter

---

## Recognition Clues
- Input is a binary array (containing only 0s and 1s).
- Find the longest contiguous segment of a single value (in this case, 1).

---

## Core Insight
- Keep a running count of the current consecutive sequence of 1s. 
- When encountering a 1, increment the count and update the maximum count. 
- When encountering a 0, reset the running count to 0 since the contiguous sequence has been broken.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all possible subarrays. For each subarray, check if it contains only 1s. If it does, compare its length with our maximum and update it if it's larger.
2. **Why Inefficient**: Generating all subarrays takes $O(N^2)$ time. Checking each one takes up to $O(N)$ time, leading to an overall $O(N^3)$ (or $O(N^2)$ if optimized) time complexity, which is highly wasteful.
3. **Key Observation**: We don't need to examine subarrays independently. A single linear scan can identify the start and end of every sequence of 1s.
4. **Optimal Solution Intuition**: 
   - Initialize two variables: `cnt = 0` (current consecutive 1s) and `max_cnt = 0` (global maximum).
   - Iterate through the array. 
   - If `num == 1`, increment `cnt` and update `max_cnt = max(max_cnt, cnt)`.
   - If `num == 0`, reset `cnt = 0`.
5. **Time Complexity**: $O(N)$ since we perform a single pass through the array.
6. **Space Complexity**: $O(1)$ auxiliary space since we only track two variables.

---

## Brute Force
- **Idea**: Check every subarray to verify if it contains only 1s, and track the maximum length.
- **Code**:
```python
def find_max_consecutive_ones_brute(nums):
    max_cnt = 0
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            all_ones = True
            for k in range(i, j + 1):
                if nums[k] != 1:
                    all_ones = False
                    break
            if all_ones:
                max_cnt = max(max_cnt, j - i + 1)
    return max_cnt
```
- **TC**: $O(N^3)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Single-pass state tracking.
  1. Set `cnt = 0` and `max_cnt = 0`.
  2. For each `num` in `nums`:
     - If `num == 1`, increment `cnt` and set `max_cnt = max(max_cnt, cnt)`.
     - Else, set `cnt = 0`.
  3. Return `max_cnt`.
- **Why it works**: By updating `max_cnt` at each step, we capture the maximum sequence length before the count is reset by a 0.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def findMaxConsecutiveOnes(nums):
    max_cnt = 0
    cnt = 0
    
    for num in nums:
        if num == 1:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
            
    return max_cnt
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [1, 1, 0, 1, 1, 1]`
  - Output: `3`
- **Hard Case**: 
  - Input: `nums = [0, 0, 0, 0]`
  - Output: `0`
- **Edge Case**: 
  - Input: `nums = [1]`
  - Output: `1`

---

## Common Mistakes
- Resetting `cnt` to 0 but failing to update `max_cnt` first (though updating `max_cnt` on every 1-encounter avoids this).
- Failing to handle arrays containing only zeros or only ones.

---

## Killer Edge Cases
- Array contains only zeros.
- Array contains only ones.
- Longest sequence of ones is at the very end of the array.

---

## Follow-Up Variants
- **Max Consecutive Ones I** $\rightarrow$ **Max Consecutive Ones II**: Allowed to flip at most one 0 to 1.
  - *Delta*: Use a sliding window where the count of zeros inside the window is $\le 1$.
- **Max Consecutive Ones II** $\rightarrow$ **Max Consecutive Ones III**: Allowed to flip at most $K$ zeros.
  - *Delta*: Expand the sliding window and contract the left pointer when zero count exceeds $K$.

---

## Similar Problems
- Max Consecutive Ones III (LeetCode 1004)
- Longest Substring Without Repeating Characters (LeetCode 3)

---

## Theory Connections
- **Finite State Automata (FSA)**: The running counter is a simple automaton where the state corresponds to the length of the current run. Transitions are triggered by symbols: `1` increments the state, `0` resets the state back to the start.

---

## Personal Progress

**Confidence**
- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5

**Time Bucket**
- [ ] <10 min
- [ ] 10-20
- [ ] 20-40
- [ ] 40+

**Status**
- [ ] Not Attempted
- [ ] Hint Used
- [ ] Solved
- [ ] Mastered

**Revision Count**: 
**Last Revised**: 
**Next Review**: 

---

## Notes

