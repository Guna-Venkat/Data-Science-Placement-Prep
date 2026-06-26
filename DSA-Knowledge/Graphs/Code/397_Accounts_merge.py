"""
LeetCode Link: https://leetcode.com/problems/accounts-merge/
Problem Name: Accounts Merge
Description: Merge email accounts belonging to the same user.

Folder: Graphs
File: 397_Accounts_merge.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Group emails under parent IDs using DisjointSet.
# Time Complexity: O(N * log N)
# Space Complexity: O(Emails)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)

def optimal_solution(accounts: list[list[str]]) -> list[list[str]]:
    ds = DisjointSet(len(accounts))
    email_to_id = {}
    for idx, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                ds.union(idx, email_to_id[email])
            else:
                email_to_id[email] = idx
                
    merged = {}
    for email, idx in email_to_id.items():
        root = ds.find(idx)
        if root not in merged:
            merged[root] = []
        merged[root].append(email)
        
    res = []
    for root, emails in merged.items():
        res.append([accounts[root][0]] + sorted(emails))
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"]]
    res = optimal_solution(accounts)
    assert len(res) == 2
    print("Done.")
