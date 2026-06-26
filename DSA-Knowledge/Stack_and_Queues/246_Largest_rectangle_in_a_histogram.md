# Largest Rectangle in a Histogram

**Pattern:** Monotonic Stack (Increasing Order)

**Recognition:**
- Find the largest rectangular area formed by contiguous histogram bars.
- The height of a rectangle is limited by the shortest bar inside its range.
- Goal is to find the First Smaller Element to the Left (NSL) and First Smaller Element to the Right (NSR) for each bar.
- Use a monotonic stack to resolve boundaries in a single $O(N)$ pass.

**Optimal Code (Python):**
```python
def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    n = len(heights)
    
    for i in range(n + 1):
        # Use a dummy height of 0 at index n to flush all remaining elements in the stack
        curr_height = heights[i] if i < n else 0
        
        while stack and heights[stack[-1]] > curr_height:
            h = heights[stack.pop()]
            # If stack is empty, it means h was the smallest height so far, width is i
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
            
        stack.append(i)
        
    return max_area
```

**Killer Edge:**
- Array is strictly increasing (e.g., `[1, 2, 3, 4, 5]`) or strictly decreasing (e.g., `[5, 4, 3, 2, 1]`).
- Contains bars of height `0`.
- All bars have identical heights.

**Mistake:**
- Incorrect width calculation formula: using `i - stack[-1]` instead of `i - stack[-1] - 1`, which counts the boundary bar incorrectly.
- Not flushing the stack at the end of the array, missing rectangles that could extend to the far right. (The dummy `0` sentinel element handles this elegantly).
