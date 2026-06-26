# Maximum XOR of Two Numbers in an Array

**Pattern:** Binary Trie (Bitwise Prefix Tree)

**Recognition:**
- Maximize the XOR sum of two numbers chosen from an array.
- Brute-force takes $O(N^2)$, which is too slow.
- To maximize the XOR sum of `x`, we want to find a number `y` whose binary digits are opposite to `x` at each bit position from most significant bit (MSB) to least significant bit (LSB).
- Insert numbers into a Binary Trie representing their 31-bit coordinates.

**Optimal Code (Python):**
```python
class TrieNode:
    def __init__(self):
        # children dict can contain keys 0 and 1
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int) -> None:
        curr = self.root
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def getMaxXOR(self, num: int) -> int:
        curr = self.root
        max_xor = 0
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            
            # Prefer path with opposite bit to maximize XOR at current level
            if opposite_bit in curr.children:
                max_xor |= (1 << i)
                curr = curr.children[opposite_bit]
            else:
                curr = curr.children[bit]
        return max_xor

def findMaximumXOR(nums: list[int]) -> int:
    trie = Trie()
    for num in nums:
        trie.insert(num)
        
    max_ans = 0
    for num in nums:
        max_ans = max(max_ans, trie.getMaxXOR(num))
        
    return max_ans
```

**Killer Edge:**
- Array elements are very small (e.g. `[0, 1]`) vs extremely large ($2^{30}-1$).
- Array contains only duplicates.

**Mistake:**
- Starting the bit loop index too low (e.g., `range(15, -1, -1)`), which fails if the numbers exceed $2^{15} - 1$. Standard constraint for integers up to $10^9$ requires 30 or 31 bits (MSB at index 30).
- Incorrectly updating `max_xor`: forgetting to set the bit using bitwise OR (`max_xor |= (1 << i)`).
