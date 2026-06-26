# Majority Element II

## Difficulty
Medium

---

## Pattern
Boyer-Moore Voting (Generalized)

---

## Recognition Clues
- Find all elements in an array that appear strictly more than $\lfloor N/3 \rfloor$ times.\n- Requires $O(N)$ time and $O(1)$ space.

---

## Core Insight
- At most two elements can appear more than $N/3$ times in any array.\n- We can generalize Boyer-Moore Voting by tracking two candidates and two counters.\n- If an element matches candidate 1 or 2, increment the corresponding counter. If counters are 0, assign candidates. Else, decrement both counters.

---

## Interview Explanation
1. **Brute Force Idea**: Use a hash map to count the frequencies of all elements. Return those elements whose frequency is strictly greater than $\lfloor N/3 floor$.
2. **Why Inefficient**: Using a hash map requires $O(N)$ space, violating the $O(1)$ space constraint.
3. **Key Observation**: Since at most two elements can appear more than $N/3$ times, we can maintain two candidates. If we encounter a third distinct element, we decrement both counters (analogous to cancelling triplets of distinct elements).
4. **Optimal Solution Intuition**:
   - Set `c1 = None`, `c2 = None`, `count1 = 0`, `count2 = 0`.
   - Iterate through elements:
     - If `num == c1`, `count1 += 1`.
     - Else if `num == c2`, `count2 += 1`.
     - Else if `count1 == 0`, `c1 = num`, `count1 = 1`.
     - Else if `count2 == 0`, `c2 = num`, `count2 = 1`.
     - Else, decrement both `count1` and `count2`.
   - Verify candidate frequencies in a second linear pass, since Boyer-Moore only promises candidates, not actual majorities.
5. **Time Complexity**: $O(N)$ (two passes).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Count frequencies of all elements using a hash map and check which exceed $N/3$.
- **Code**:
```python
def majorityElementII_brute(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    ans = []
    for num, count in counts.items():
        if count > len(nums) // 3:
            ans.append(num)
    return ans
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: Generalized Boyer-Moore Voting Algorithm.
- **Why it works**: Three-way cancellations preserve the dominance of elements that appear more than $1/3$ of the time.
- **Complexity**: Time: $O(N)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def majorityElementII(nums):
    if not nums:
        return []
        
    c1, c2 = None, None
    count1, count2 = 0, 0
    
    # 1. Find candidates
    for num in nums:
        if num == c1:
            count1 += 1
        elif num == c2:
            count2 += 1
        elif count1 == 0:
            c1 = num
            count1 = 1
        elif count2 == 0:
            c2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
            
    # 2. Verify candidates
    ans = []
    for cand in [c1, c2]:
        if cand is not None:
            # Check actual count in array
            if nums.count(cand) > len(nums) // 3:
                ans.append(cand)
                
    return list(set(ans))
```

---

## Test Cases
- **Normal Case**: Input: `nums = [3, 2, 3]`\n- Output: `[3]`
- **Hard Case**: Input: `nums = [1, 2, 3, 1, 2, 1, 2]`\n- Output: `[1, 2]`
- **Edge Case**: Input: `nums = [1]`\n- Output: `[1]`

---

## Common Mistakes
- Not implementing the verification step (mandatory because the algorithm can select elements that do not exceed $N/3$ if no actual majorities exist).\n- Wrong candidate checks order (e.g. checking `count == 0` before checking if the element matches the other candidate, which leads to duplicate candidates).

---

## Killer Edge Cases
- Only one majority element exists.\n- No majority elements exist.\n- Array has duplicates of candidates.

---

## Follow-Up Variants
- Majority Element II (threshold $N/3$) $\rightarrow$ Majority Element K (threshold $N/K$).

---

## Similar Problems
- Majority Element I\n- Top K Frequent Elements

---

## Theory Connections
- Misra-Gries Summary Algorithm: A generalization of Boyer-Moore for finding items in data streams exceeding $N/k$ frequency using $O(k)$ memory. It forms the base of heavy hitter estimations in big data systems.

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
