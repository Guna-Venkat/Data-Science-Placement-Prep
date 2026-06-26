import os
import re

# Solution dictionary for the 7 basic problems
BASIC_SOLUTIONS = {
    "037_Reverse_a_number.md": """# Reverse a number

## Difficulty
Easy

## Pattern
Basic Math / Digit Extraction

## Optimal Code (Python)
```python
def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    
    # 32-bit signed integer range bounds check
    if rev > 2**31 - 1:
        return 0
    return sign * rev
```

## Complexity
- Time Complexity: $O(\\log_{10} N)$
- Space Complexity: $O(1)$
""",

    "038_Palindrome_Number.md": """# Palindrome Number

## Difficulty
Easy

## Pattern
Basic Math / Digit Extraction

## Optimal Code (Python)
```python
def is_palindrome(n: int) -> bool:
    if n < 0:
        return False
    
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
        
    return original == rev
```

## Complexity
- Time Complexity: $O(\\log_{10} N)$
- Space Complexity: $O(1)$
""",

    "039_GCD_of_Two_Numbers.md": """# GCD of Two Numbers

## Difficulty
Easy

## Pattern
Euclidean Algorithm

## Optimal Code (Python)
```python
def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a
```

## Complexity
- Time Complexity: $O(\\log(\\min(a, b)))$
- Space Complexity: $O(1)$
""",

    "051_Fibonacci_Number.md": """# Fibonacci Number

## Difficulty
Easy

## Pattern
Iteration / DP Space Optimized

## Optimal Code (Python)
```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    prev2, prev = 0, 1
    for _ in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev
```

## Complexity
- Time Complexity: $O(N)$
- Space Complexity: $O(1)$
""",

    "055_Selection_Sort.md": """# Selection Sort

## Difficulty
Easy

## Pattern
Sorting

## Optimal Code (Python)
```python
def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

## Complexity
- Time Complexity: $O(N^2)$
- Space Complexity: $O(1)$
""",

    "056_Bubble_Sort.md": """# Bubble Sort

## Difficulty
Easy

## Pattern
Sorting

## Optimal Code (Python)
```python
def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1, 0, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if not did_swap:
            break
    return arr
```

## Complexity
- Time Complexity: $O(N^2)$ worst/average, $O(N)$ best case
- Space Complexity: $O(1)$
""",

    "058_Merge_Sorting.md": """# Merge Sort

## Difficulty
Medium

## Pattern
Divide and Conquer / Sorting

## Optimal Code (Python)
```python
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
        
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

## Complexity
- Time Complexity: $O(N \\log N)$
- Space Complexity: $O(N)$
"""
}

# The 20 hardest problems (should be protected from placeholders if we run the script)
HARD_IDS = {
    '422', '427', '435', '437', '443', '450', '380', '388', '389', '393', 
    '122', '123', '127', '246', '251', '322', '332', '471', '464', '199'
}

def main():
    dsa_dir = os.path.join(".", "DSA-Knowledge")
    
    updated_count = 0
    placeholder_count = 0
    
    for root, dirs, files in os.walk(dsa_dir):
        # Skip CheatSheets directory
        if "00_CheatSheets" in root:
            continue
        
        # Skip the Arrays folder completely to preserve existing manual refactorings
        if "Arrays" in root:
            continue
            
        for file in files:
            # Check if it matches ID format
            match = re.match(r"^(\d+)_(.+)\.md$", file)
            if not match:
                continue
                
            problem_id = match.group(1)
            file_path = os.path.join(root, file)
            
            # If it's one of the 20 hard reference files, skip
            if problem_id in HARD_IDS:
                continue
                
            # Check if file has basic solution
            if file in BASIC_SOLUTIONS:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(BASIC_SOLUTIONS[file])
                updated_count += 1
            else:
                # Check if file is empty, or only contains basic/default templates
                # Let's inspect size
                try:
                    size = os.path.getsize(file_path)
                except OSError:
                    size = 0
                    
                # If size is small (e.g. < 500 bytes) or we just want to ensure a placeholder, overwrite
                # (You can adjust this logic if needed when running)
                if size < 500:
                    title_name = match.group(2).replace("_", " ")
                    placeholder_content = f"# {title_name}\n\n<!-- TODO: Add Optimal Solution -->\n"
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(placeholder_content)
                    placeholder_count += 1
                    
    print(f"Dry run info: Overwrote {updated_count} basic files. Placed stubs in {placeholder_count} empty files.")

if __name__ == "__main__":
    main()
