"""
LeetCode Link: N/A
Problem Name: Minimum Spanning Tree Theory
Description: Conceptual verification of MST vertices and edges properties.

Folder: Graphs
File: 391_MST_theory.py
"""

# ============================================
# CONCEPT
# ============================================
# For connected undirected graph G with V vertices:
# MST contains V vertices and V - 1 edges. No cycles.
def verify():
    # If V=3, MST contains 2 edges.
    assert 3 - 1 == 2

if __name__ == "__main__":
    print("Running tests...")
    verify()
    print("Done.")
