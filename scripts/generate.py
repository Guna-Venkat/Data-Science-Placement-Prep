import os
import re
import csv

# Mapping of Problem ID/Name to its LeetCode URL and Description
# Only fill this for the toughest ~20 problems. The rest will get a generic stub.
PROBLEM_META = {
    "122_Aggressive_Cows": {
        "url": "https://www.geeksforgeeks.org/aggressive-cows-problem/",
        "desc": "Place cows in stalls with maximum minimum distance."
    },
    "123_Book_Allocation_Problem": {
        "url": "https://www.geeksforgeeks.org/allocate-minimum-number-pages/",
        "desc": "Allocate books to students minimizing max pages."
    },
    "127_Median_of_2_sorted_arrays": {
        "url": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
        "desc": "Find median of two sorted arrays in O(log(min(n,m))) time."
    },
    "246_Largest_rectangle_in_a_histogram": {
        "url": "https://leetcode.com/problems/largest-rectangle-in-histogram/",
        "desc": "Find max rectangle area in a histogram."
    },
    "251_LRU_Cache": {
        "url": "https://leetcode.com/problems/lru-cache/",
        "desc": "Implement LRU Cache using Doubly Linked List + HashMap."
    },
    "322_LCA_in_BT": {
        "url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
        "desc": "Find LCA of two nodes in a binary tree."
    },
    "332_Morris_Preorder_Traversal": {
        "url": "https://leetcode.com/problems/binary-tree-preorder-traversal/",
        "desc": "Morris traversal for O(1) space preorder."
    },
    "380_Djikstras_Algorithm": {
        "url": "https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/",
        "desc": "Find shortest path from source to all nodes."
    },
    "388_Bellman_Ford_Algorithm": {
        "url": "https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/",
        "desc": "Find shortest path handling negative weights."
    },
    "389_Floyd_warshall_algorithm": {
        "url": "https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/",
        "desc": "All-pairs shortest path using DP."
    },
    "393_Disjoint_Set": {
        "url": "https://www.geeksforgeeks.org/disjoint-set-data-structures/",
        "desc": "Union-Find data structure with path compression."
    },
    "422_Minimum_Coins_DP_20": {
        "url": "https://leetcode.com/problems/coin-change/",
        "desc": "Find minimum coins to make amount using unlimited coins."
    },
    "427_Longest_common_subsequence": {
        "url": "https://leetcode.com/problems/longest-common-subsequence/",
        "desc": "DP for LCS of two strings."
    },
    "435_Edit_distance": {
        "url": "https://leetcode.com/problems/edit-distance/",
        "desc": "Minimum operations to convert word1 to word2."
    },
    "437_Best_time_to_buy_and_sell_stock": {
        "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "desc": "Max profit with at most one transaction."
    },
    "443_Longest_Increasing_Subsequence": {
        "url": "https://leetcode.com/problems/longest-increasing-subsequence/",
        "desc": "Find LIS using patience sorting / DP."
    },
    "450_Matrix_chain_multiplication": {
        "url": "https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/",
        "desc": "Minimize cost of multiplying matrices using MCM DP."
    },
    "464_Maximum_XOR_of_two_numbers_in_an_array": {
        "url": "https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/",
        "desc": "Use Trie to find max XOR pair."
    },
    "471_KMP_Algorithm_or_LPS_array": {
        "url": "https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/",
        "desc": "Knuth-Morris-Pratt pattern matching."
    },
    "199_N_Queen": {
        "url": "https://leetcode.com/problems/n-queens/",
        "desc": "Place N queens on NxN chessboard without attacking."
    }
}

TOPICS = [
    "Arrays", "Binary_Search", "Binary_Search_Trees", "Binary_Trees",
    "Bit_Manipulation", "Dynamic_Programming", "Graphs", "Greedy_Algorithms",
    "Heaps", "Learn_the_Basics", "LinkedList", "Recursion",
    "Sliding_Window_and_Two_Pointer", "Sorting_Techniques",
    "Stack_and_Queues", "Strings", "Strings_Advanced", "Tries"
]

def generate_code_content(file_name, folder):
    """Generate Python code with LeetCode link, description, Brute, Optimal, and tests."""
    id_match = re.search(r'^(\d+)', file_name)
    prob_id = id_match.group(1) if id_match else "000"
    base_name = file_name.replace(f"{prob_id}_", "").replace(".md", "").replace("|", "_")
    meta = PROBLEM_META.get(f"{prob_id}_{base_name}", None) or PROBLEM_META.get(f"{prob_id}_{base_name.split('_')[0]}", None)
    
    if not meta:
        meta = {"url": "https://leetcode.com/problems/.../", "desc": "Problem description goes here."}
    
    title = base_name.replace("_", " ")
    
    return f'''"""
LeetCode Problem: {meta["url"]}
Problem Name: {title}
Description: {meta["desc"]}

Folder: {folder}
File: {file_name}
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: [Explain brute force logic here]
# Time Complexity: O(?)
# Space Complexity: O(?)
def brute_force_solution():
    # TODO: Implement brute force
    pass

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: [Explain the main trick/efficiency]
# Time Complexity: O(?)
# Space Complexity: O(?)
def optimal_solution():
    # TODO: Implement optimal solution
    pass

# ============================================
# TEST CASES (Run this file to verify)
# ============================================
if __name__ == "__main__":
    print(f"Running tests for {title}...")
    
    # Test Case 1: [Description]
    # Expected Output: [Value]
    # print(optimal_solution(...))
    
    # Test Case 2: [Edge Case Description]
    # Expected Output: [Value]
    # print(optimal_solution(...))
    
    print("Done.")
'''

def restructure():
    # Step 1: Create new structure & move files
    for topic in TOPICS:
        if not os.path.exists(topic):
            continue
            
        # Create subfolders
        os.makedirs(os.path.join(topic, "Code"), exist_ok=True)
        os.makedirs(os.path.join(topic, "Md"), exist_ok=True)
        os.makedirs(os.path.join(topic, "Miscellaneous"), exist_ok=True)
        
        # Move existing .md files into Md/
        for file in os.listdir(topic):
            src = os.path.join(topic, file)
            if os.path.isfile(src) and file.endswith(".md"):
                dest = os.path.join(topic, "Md", file)
                os.rename(src, dest)
                print(f"Moved {file} -> {topic}/Md/")
                
                # Generate corresponding .py file in Code/
                py_name = file.replace(".md", ".py")
                py_path = os.path.join(topic, "Code", py_name)
                if not os.path.exists(py_path):
                    with open(py_path, 'w') as f:
                        f.write(generate_code_content(file, topic))
                    print(f"Generated {py_path}")
        
        # Create tracker.csv
        tracker_path = os.path.join(topic, "tracker.csv")
        if not os.path.exists(tracker_path):
            with open(tracker_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Problem", "Difficulty", "Pattern", "Status", "Time_Complexity", "Space_Complexity"])
                # Populate with existing files if possible
                md_files = sorted([f for f in os.listdir(os.path.join(topic, "Md")) if f.endswith(".md")])
                for f in md_files:
                    prob_name = f.replace(".md", "")
                    writer.writerow([prob_name.split("_")[0], prob_name, "", "", "", "", ""])
            print(f"Created {tracker_path}")
        
        # Create notes.md
        notes_path = os.path.join(topic, "notes.md")
        if not os.path.exists(notes_path):
            with open(notes_path, 'w') as f:
                f.write(f"# {topic} - Topic Notes\n\n## Patterns Learned\n- [TBD]\n\n## Common Mistakes in {topic}\n- [TBD]\n\n## Edge Cases Specific to {topic}\n- [TBD]\n\n## Revision History\n\n")
            print(f"Created {notes_path}")

if __name__ == "__main__":
    restructure()
    print("\n✅ Restructuring complete! Your repo now has Code/, Md/, Miscellaneous/, tracker.csv, and notes.md for every topic.")
    print("📂 Check the 'Code' folders—the top 20 hardest problems already have detailed skeletons with LeetCode links.")