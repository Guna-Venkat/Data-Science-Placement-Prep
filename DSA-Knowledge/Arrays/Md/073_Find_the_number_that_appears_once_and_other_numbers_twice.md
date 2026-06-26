# Find the number that appears once and other numbers twice

## Difficulty
Easy

---

## Pattern
Bitwise XOR (Single Number)

---

## Recognition Clues
- Every element in the array appears exactly twice, except for one element which appears only once.
- Goal is to find the single element in $O(N)$ time and $O(1)$ space.

---

## Core Insight
- **XOR Properties**: 
  - $x \oplus x = 0$ (Any number XORed with itself is 0)
  - $x \oplus 0 = x$ (Any number XORed with 0 is itself)
  - XOR is associative and commutative.
- XORing all elements together cancels out all pairs, leaving the single element.

---

## Interview Explanation
1. **Brute Force Idea**: Use a hash map to count the frequencies of all numbers. Iterate through the hash map and return the key with a frequency count of 1.
2. **Why Inefficient**: Utilizing a hash map requires $O(N)$ auxiliary space, which violates the $O(1)$ space constraint.
3. **Key Observation**: Since all duplicates appear an even number of times (exactly twice), we can use the bitwise XOR operation to cancel out the duplicates without storing them.
4. **Optimal Solution Intuition**: Initialize a variable `xor_sum = 0`. Loop through all elements in the array and perform `xor_sum ^= num`. The elements that appear twice will cancel out to 0, leaving only the single number in `xor_sum`.
5. **Time Complexity**: $O(N)$ because we make a single linear pass.
6. **Space Complexity**: $O(1)$ because we only use one variable.

---

## Brute Force
- **Idea**: Use a hash map to keep track of counts and return the element with count 1.
- **Code**:
```python
def find_single_number_brute(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    for num, count in counts.items():
        if count == 1:
            return num
            
    return -1
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: XOR Accumulation.
  1. Set `xor_sum = 0`.
  2. For every number `num` in `nums`, compute `xor_sum ^= num`.
  3. Return `xor_sum`.
- **Why it works**: By commutativity, the XOR sequence can be rearranged as: $(A_1 \oplus A_1) \oplus (A_2 \oplus A_2) \dots \oplus S$, where $S$ is the single element. This simplifies to $0 \oplus 0 \dots \oplus S = S$.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def singleNumber(nums):
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    return xor_sum
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [4, 1, 2, 1, 2]`
  - Output: `4`
- **Hard Case**: 
  - Input: `nums = [-10**9, -10**9, -5]`
  - Output: `-5`
- **Edge Case**: 
  - Input: `nums = [1]`
  - Output: `1`

---

## Common Mistakes
- Initializing `xor_sum` to `1` or another non-zero value.
- Attempting to sort the array first, which increases the time complexity to $O(N \log N)$.

---

## Killer Edge Cases
- Array contains only 1 element.
- Single number is negative or zero.

---

## Follow-Up Variants
- **Single Number I** $\rightarrow$ **Single Number II**: Every element appears three times except one which appears once.
  - *Delta*: Count the sum of bits at each position modulo 3, or use two bitmasks (`ones`, `twos`) to track states.
- **Single Number I** $\rightarrow$ **Single Number III**: Every element appears twice except two numbers which appear once.
  - *Delta*: Find the total XOR sum $X \oplus Y$. Partition the array based on the rightmost set bit in $X \oplus Y$ to isolate $X$ and $Y$ in separate partitions.

---

## Similar Problems
- Single Number II (LeetCode 137)
- Single Number III (LeetCode 260)

---

## Theory Connections
- **Self-Inverse Operations**: XOR is a self-inverse function (an involution). In algebra, involutions are used for fast bit manipulation, data checksums, and cryptography (such as in stream ciphers where encryption and decryption use the same XOR operation).

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

