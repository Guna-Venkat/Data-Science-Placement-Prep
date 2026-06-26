"""
LeetCode Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Problem Name: All Nodes Distance K in Binary Tree
Description: Find all nodes at distance K from a target node.

Folder: Binary_Trees
File: 325_Print_all_nodes_at_a_distance_of_K_in_BT.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep parent pointers. Run BFS from target in 3 directions (left, right, parent).
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    parents = {}
    
    # 1. Map parent pointers
    def map_parents(node, parent=None):
        if not node:
            return
        parents[node] = parent
        map_parents(node.left, node)
        map_parents(node.right, node)
        
    map_parents(root)
    
    # 2. BFS from target
    queue = [(target, 0)]
    visited = {target}
    result = []
    
    while queue:
        node, dist = queue.pop(0)
        if dist == k:
            result.append(node.val)
            continue
            
        for neighbor in (node.left, node.right, parents[node]):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
    
    res = optimal_solution(root, target, 2)
    assert sorted(res) == sorted([7, 4, 1])
    print("Done.")
