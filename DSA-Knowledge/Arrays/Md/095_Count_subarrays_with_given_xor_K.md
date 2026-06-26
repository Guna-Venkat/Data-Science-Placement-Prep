# Count subarrays with given xor K

## Difficulty
Medium

---

## Pattern
Prefix XOR / Hashing (Frequency)

---

## Recognition Clues
- Count total number of subarrays whose bitwise XOR sum is exactly $K$.\n- Involves positive integers.

---

## Core Insight
- Let prefix XOR up to index $i$ be $XR_i$. The XOR of subarray from $j+1$ to $i$ is $XR_i \oplus XR_j$.\n- If $XR_i \oplus XR_j = K$, then $XR_j = XR_i \oplus K$ (applying XOR to both sides).\n- We can maintain the running frequencies of prefix XOR values in a Hash Map and look up `curr_xor ^ K` at each index.

---

## Interview Explanation
1. **Brute Force Idea**: Check all subarrays using two nested loops. Calculate the XOR sum of each subarray and increment the count if it equals $K$.
2. **Why Inefficient**: Takes $O(N^2)$ time.
3. **Key Observation**: XOR is self-inverting: if $A \oplus B = C$, then $A \oplus C = B$. If the cumulative XOR at index $i$ is `curr_xor`, we want to find how many previous indices $j$ had prefix XOR equal to `curr_xor ^ K`.
4. **Optimal Solution Intuition**:
   - Maintain a running prefix XOR `curr_xor` and a hash map `pre_map` mapping `prefix_xor -> frequency`. Initialize `pre_map = {0: 1}`.
   - Iterate through the array. For each element:
     - `curr_xor ^= num`.
     - Add `pre_map[curr_xor ^ K]` to `count` if it exists.
     - Update `pre_map[curr_xor] = pre_map.get(curr_xor, 0) + 1`.
5. **Time Complexity**: $O(N)$ (single pass).
6. **Space Complexity**: $O(N)$ to store prefix XORs in the map.

---

## Brute Force
- **Idea**: Evaluate XOR sum of all possible subarrays.
- **Code**:
```python
def solve_brute(A, B):
    count = 0
    n = len(A)
    for i in range(n):
        curr_xor = 0
        for j in range(i, n):
            curr_xor ^= A[j]
            if curr_xor == B:
                count += 1
    return count
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Prefix XOR hashing with frequency tracking.
- **Why it works**: Using the algebraic property $XR_j = XR_i \oplus K$ lets us locate all qualifying left boundaries for the current XOR window in $O(1)$ time.
- **Complexity**: Time: $O(N)$, Space: $O(N)$.

---

## Optimal Code
```python
def solve(A, B):
    pre_map = {0: 1}  # Base case: XOR sum of 0 seen 1 time
    curr_xor = 0
    count = 0
    
    for num in A:
        curr_xor ^= num
        target = curr_xor ^ B
        
        # If target XOR exists in map, add its frequency
        if target in pre_map:
            count += pre_map[target]
            
        # Update prefix XOR frequency
        pre_map[curr_xor] = pre_map.get(curr_xor, 0) + 1
        
    return count
```

---

## Test Cases
- **Normal Case**: Input: `A = [4, 2, 2, 6, 4]`, `B = 6`\n- Output: `4` (subarrays are `[4, 2]`, `[6]`, `[2, 2, 6]`, `[6, 4]` and `[4, 2, 2, 6, 4]`? Let's check: 4^2=6, 6=6, 2^2^6=6, 6^4=2 (no), 4^2^2^6^4 = 6^2^6^4 = 4^6^4 = 6. Correct. Count is 4.)
- **Hard Case**: Input: `A = [5, 6, 7, 8, 9]`, `B = 5`\n- Output: `2`
- **Edge Case**: Input: `A = [0]`, `B = 0`\n- Output: `1`

---

## Common Mistakes
- Using subtraction or addition instead of XOR (`curr_xor - K` instead of `curr_xor ^ K`).\n- Forgetting to initialize the map with `{0: 1}`.

---

## Killer Edge Cases
- K = 0.\n- Array contains zeros (which do not change the XOR value but increase the count of subarrays).\n- No subarrays match the XOR sum.

---

## Follow-Up Variants
- Count Subarrays with XOR K $\rightarrow$ Longest Subarray with XOR K

---

## Similar Problems
- Subarray Sum Equals K\n- Subarray Sums Divisible by K

---

## Theory Connections
- Group Inverses: The set of binary integers under XOR forms a group where every element is its own inverse. This allows resolving target sums via transposition: $X \oplus Y = K \iff X \oplus K = Y$, which is not possible in general algebraic structures without inverse elements.

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
