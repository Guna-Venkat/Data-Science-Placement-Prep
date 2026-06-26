# Majority Element I

## Difficulty
Medium

---

## Pattern
Boyer-Moore Voting Algorithm

---

## Recognition Clues
- Find the element in an array that appears strictly more than $\lfloor N/2 \rfloor$ times.
- Require $O(N)$ time complexity and $O(1)$ auxiliary space.

---

## Core Insight
- Because the majority element appears more than $N/2$ times, it can outvote all other distinct elements combined.
- If we pair up distinct elements and cancel them out, the majority element is guaranteed to survive as the candidate at the end of the process.

---

## Interview Explanation
1. **Brute Force Idea**: Use a hash map to count the occurrences of each element. Iterate through the hash map and return the element whose frequency is strictly greater than $\lfloor N/2 \rfloor$.
2. **Why Inefficient**: Utilizing a hash map requires $O(N)$ auxiliary space, which violates the $O(1)$ space requirement.
3. **Key Observation**: If we cancel out two different elements, the majority element's dominant ratio ($> 50\%$) is preserved in the remaining subarray.
4. **Optimal Solution Intuition (Boyer-Moore)**:
   - Maintain a `candidate` and a `count` variable initialized to `0`.
   - Loop through the array. For each element `num`:
     - If `count == 0`, assign `candidate = num` and set `count = 1`.
     - Else, if `num == candidate`, increment `count` by 1.
     - Else, decrement `count` by 1.
   - (Verification step): If the problem does not guarantee a majority element exists, run a second linear pass to count occurrences of `candidate` and verify if it exceeds $\lfloor N/2 \rfloor$.
5. **Time Complexity**: $O(N)$ (requires one pass to find the candidate and one optional pass to verify).
6. **Space Complexity**: $O(1)$ auxiliary space since we only store two scalar variables.

---

## Brute Force
- **Idea**: Count frequencies of all elements using a hash map and check which exceeds $N/2$.
- **Code**:
```python
def majority_element_brute(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    for num, count in counts.items():
        if count > len(nums) // 2:
            return num
            
    return -1
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: Boyer-Moore Voting Algorithm.
  1. Initialize `candidate = None` and `count = 0`.
  2. For `num` in `nums`:
     - If `count == 0`, set `candidate = num`.
     - If `num == candidate`, increment `count`.
     - Else, decrement `count`.
  3. Optionally, check if `candidate` appears $> N/2$ times. If so, return it.
- **Why it works**: Discarding distinct pairs reduces array size by 2, but can decrease the count of the majority element by at most 1. The majority element still dominates the remainder.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def majorityElement(nums):
    candidate = None
    count = 0
    
    # Step 1: Find the majority candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
    # Step 2: Verification pass (highly recommended in interviews)
    verification_count = 0
    for num in nums:
        if num == candidate:
            verification_count += 1
            
    if verification_count > len(nums) // 2:
        return candidate
        
    return -1  # If no majority element exists
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [2, 2, 1, 1, 1, 2, 2]`
  - Output: `2`
- **Hard Case**: 
  - Input: `nums = [1, 2, 3, 3, 3, 3, 4]` (size $N=7$, majority element is 3)
  - Output: `3`
- **Edge Case**: 
  - Input: `nums = [42]`
  - Output: `42`

---

## Common Mistakes
- Resetting the candidate but forgetting to set the count back to 1.
- Not verifying the candidate when the problem statement does not guarantee the existence of a majority element.

---

## Killer Edge Cases
- No majority element exists in the array.
- Array contains alternating elements (`[1, 2, 1, 2, 1]`).
- Array size is 1.

---

## Follow-Up Variants
- **Majority Element I** $\rightarrow$ **Majority Element II**: Find all elements that appear strictly more than $\lfloor N/3 \rfloor$ times.
  - *Delta*: Generalize to support at most two candidates and two counters.

---

## Similar Problems
- Majority Element II (LeetCode 229)
- Check If a Number Is Majority Element in a Sorted Array (LeetCode 1150)

---

## Theory Connections
- **Streaming Algorithms**: Boyer-Moore is a classic streaming algorithm. It solves the majority problem in $O(1)$ working memory, which is essential in systems where data packets are processed in real-time (such as IP packet headers in network routers or clickstream logs).

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

