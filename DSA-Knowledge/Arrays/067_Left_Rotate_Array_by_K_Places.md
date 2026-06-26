# Left Rotate Array by K Places

## Difficulty
Easy

---

## Pattern
Array Reversal / Segment Swap

---

## Recognition Clues
- Shift array elements to the left by an arbitrary number of steps $K$.
- Requires performing the shift in-place with $O(1)$ auxiliary space.

---

## Core Insight
- To left-rotate an array by $K$ elements, we can reverse the first $K$ elements, reverse the remaining $N-K$ elements, and then reverse the entire array. Reversing twice preserves the relative ordering of the elements while moving the partition.

---

## Interview Explanation
1. **Brute Force Idea**: Copy the first $K$ elements of the array into a temporary array `temp`. Shift the remaining $N-K$ elements of the array to the left by $K$ positions. Then, copy the elements from `temp` back into the last $K$ positions of the array.
2. **Why Inefficient**: Storing the first $K$ elements in `temp` requires $O(K)$ extra space, which scales up to $O(N)$ when $K \approx N$.
3. **Key Observation**: Reversal is a self-inverting operation. If we reverse the prefix and suffix independently, they are internally backwards. Reversing the entire array swaps the prefix and suffix positions and also flips them back to their original relative order.
4. **Optimal Solution Intuition**: 
   - Take $K = K \pmod N$ (since rotating by $N$ steps results in the original array).
   - Reverse the prefix `arr[0...K-1]`.
   - Reverse the suffix `arr[K...N-1]`.
   - Reverse the entire array `arr[0...N-1]`.
5. **Time Complexity**: $O(N)$ because each element is swapped a constant number of times.
6. **Space Complexity**: $O(1)$ auxiliary space since swaps are performed in-place.

---

## Brute Force
- **Idea**: Store the first $K$ elements in a temporary list, shift the rest, and restore from the list.
- **Code**:
```python
def left_rotate_k_brute(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    temp = arr[:k]
    
    # Shift remaining elements left
    for i in range(k, n):
        arr[i - k] = arr[i]
        
    # Copy temp elements to the end
    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]
        
    return arr
```
- **TC**: $O(N)$
- **SC**: $O(K)$

---

## Optimal Approach
- **Algorithm**: 
  1. Calculate `k = k % n`.
  2. Implement an in-place helper function `reverse(start, end)` to swap elements from `start` to `end`.
  3. Call `reverse(0, k - 1)`.
  4. Call `reverse(k, n - 1)`.
  5. Call `reverse(0, n - 1)`.
- **Why it works**: Reversing the segments first aligns their elements so that when the entire array is reversed, the segments end up in the correct location and orientation.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def rotate_left(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)
    # Reverse the whole array
    reverse(0, n - 1)
    
    return arr
```

---

## Test Cases
- **Normal Case**: 
  - Input: `arr = [1, 2, 3, 4, 5]`, `k = 2`
  - Output: `[3, 4, 5, 1, 2]`
- **Hard Case**: 
  - Input: `arr = [1, 2]`, `k = 5`
  - Output: `[2, 1]` (Since `5 % 2 == 1`, same as rotating by 1)
- **Edge Case**: 
  - Input: `arr = [42]`, `k = 100`
  - Output: `[42]`

---

## Common Mistakes
- Out of bounds access if `k` is not reduced modulo $N$ (`k = k % n`).
- Off-by-one errors when defining boundaries for index segments (e.g., reversing up to `k` instead of `k - 1`).

---

## Killer Edge Cases
- `k` is larger than the array length.
- Array size is 0 or 1.
- `k` is 0 or a multiple of $N$ (no-op).

---

## Follow-Up Variants
- **Left Rotate by K** $\rightarrow$ **Right Rotate by K**: Rotate elements to the right instead of the left.
  - *Delta*: Reverse the suffix `arr[N-K...N-1]` first, then prefix `arr[0...N-K-1]`, then the whole array.

---

## Similar Problems
- Rotate Array (LeetCode 189 - Right Rotate version)
- Rotate List

---

## Theory Connections
- **Group Theory & Permutations**: Left rotation is a cyclic shift permutation. The reversal method is a classic application of symmetric group properties, showing how transposition generators can implement cycle shifting.

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

