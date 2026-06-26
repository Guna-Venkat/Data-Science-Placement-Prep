# Find missing number

## Difficulty
Easy

---

## Pattern
Bitwise XOR / Mathematical Sum

---

## Recognition Clues
- Input is an array containing $N-1$ distinct integers in the range $[1, N]$ (or $N$ integers in the range $[0, N]$).
- Exactly one number is missing from the sequence.

---

## Core Insight
- **XOR property**: Since $x \oplus x = 0$ and $x \oplus 0 = x$, XORing all numbers from $1$ to $N$ with all numbers in the array will cancel out all duplicate elements, leaving only the missing number.
- **Sum property**: The mathematical sum of the first $N$ natural numbers is $S_N = \frac{N(N+1)}{2}$. Subtracting the sum of elements in the array from $S_N$ gives the missing number.

---

## Interview Explanation
1. **Brute Force Idea**: For every integer from $1$ to $N$, perform a linear search in the array. If an integer is not found, it is the missing number.
2. **Why Inefficient**: Performing a linear search of size $N$ for $N$ different elements takes $O(N^2)$ time, which is highly suboptimal.
3. **Key Observation**: The elements in the array are a subset of the first $N$ integers. We can aggregate both sets (the full range and the array) using summation or XOR to find the difference in a single pass.
4. **Optimal Solution Intuition (XOR-based)**:
   - Compute the XOR sum of all numbers from $1$ to $N$ (let this be `xor1`).
   - Compute the XOR sum of all numbers present in the array (let this be `xor2`).
   - The missing number is `xor1 ^ xor2`.
   - *Note*: XOR is preferred over the summation formula ($\frac{N(N+1)}{2}$) because it avoids integer overflow in languages with fixed-width integers (like C++ or Java).
5. **Time Complexity**: $O(N)$ because we scan the numbers up to $N$ and the array once.
6. **Space Complexity**: $O(1)$ auxiliary space since we only store XOR running totals.

---

## Brute Force
- **Idea**: Perform linear search for each number in the range.
- **Code**:
```python
def find_missing_brute(arr, n):
    for i in range(1, n + 1):
        found = False
        for num in arr:
            if num == i:
                found = True
                break
        if not found:
            return i
    return -1
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: XOR-based cancellation.
  1. Initialize `xor1 = 0` and `xor2 = 0`.
  2. Loop $i$ from $1$ to $N$ and set `xor1 ^= i`.
  3. Loop through all elements in the array and XOR them into `xor2`.
  4. Return `xor1 ^ xor2`.
- **Why it works**: Every number present in the array appears twice (once in `xor1` and once in `xor2`), which cancels to 0. The missing number appears only once (in `xor1`), so it remains.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def missingNumber(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    
    # XOR all numbers in the full range [1, N]
    for i in range(1, n + 1):
        xor1 ^= i
        
    # XOR all numbers in the array
    for num in nums:
        xor2 ^= num
        
    return xor1 ^ xor2
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [3, 0, 1]` (size $N=3$, range $[0, 3]$)
  - Output: `2`
- **Hard Case**: 
  - Input: `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`
  - Output: `8`
- **Edge Case**: 
  - Input: `nums = [0]`
  - Output: `1`

---

## Common Mistakes
- Off-by-one error regarding the range (e.g. $[0, N]$ vs $[1, N]$).
- Integer overflow in standard Java/C++ when using the sum formula $\frac{N(N+1)}{2}$ if $N > 65535$ (for 32-bit signed integers). Always prefer XOR or use 64-bit integer types.

---

## Killer Edge Cases
- Missing element is the maximum number $N$.
- Missing element is the minimum number $0$ (or $1$).
- Array size is 1.

---

## Follow-Up Variants
- **Find One Missing Number** $\rightarrow$ **Find Two Missing Numbers**: Find two missing numbers in the range $[1, N]$.
  - *Delta*: Compute the XOR sum of the array and range. The result is $X \oplus Y$. Find the rightmost set bit in $X \oplus Y$, and divide the array and range into two groups to isolate and find $X$ and $Y$ separately.

---

## Similar Problems
- Single Number (LeetCode 136)
- Find the Duplicate Number (LeetCode 287)

---

## Theory Connections
- **Algebraic Group Theory**: The set of integers under the XOR operation $\oplus$ forms an Abelian Group, where the identity element is 0 and every element is its own inverse ($A \oplus A = 0$). This property makes XOR a powerful tool in error correction codes (parity check, RAID) and cryptography.

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

