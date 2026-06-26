import csv
import os

TRACKER_DATA = [
    ["335", "335_Introduction_to_BST", "Easy", "Basic BST", "Completed", "O(N)", "O(1)"],
    ["336", "336_Search_in_a_Binary_Search_Tree", "Easy", "BST Properties", "Completed", "O(H)", "O(1)"],
    ["337", "337_Find_Min_Max_in_BST", "Easy", "BST Properties", "Completed", "O(H)", "O(1)"],
    ["338", "338_Ceil_in_a_BST", "Medium", "BST Search", "Completed", "O(H)", "O(1)"],
    ["339", "339_Floor_in_a_BST", "Medium", "BST Search", "Completed", "O(H)", "O(1)"],
    ["340", "340_Insert_a_given_Node_in_BST", "Easy", "BST Modification", "Completed", "O(H)", "O(1)"],
    ["341", "341_Delete_a_Node_in_BST", "Medium", "BST Modification", "Completed", "O(H)", "O(H)"],
    ["342", "342_Find_Kth_smallest_largest_element_in_BST", "Medium", "Inorder Traversal", "Completed", "O(N)", "O(H)"],
    ["343", "343_Check_if_a_tree_is_BST_or_not", "Medium", "Recursion / Range check", "Completed", "O(N)", "O(H)"],
    ["344", "344_LCA_in_BST", "Easy", "BST Properties", "Completed", "O(H)", "O(1)"],
    ["345", "345_Construct_BST_from_preorder_traversal", "Medium", "Recursion / range check", "Completed", "O(N)", "O(H)"],
    ["346", "346_Inorder_Successor_Predecessor_in_BST", "Medium", "BST Search", "Completed", "O(H)", "O(1)"],
    ["347", "347_Binary_Search_Tree_Iterator", "Medium", "Inorder Traversal / Stack", "Completed", "O(1) amortized", "O(H)"],
    ["348", "348_Two_Sum_In_BST_or_Find_a_pair_with_given_sum_in_BST", "Medium", "Inorder Iterator", "Completed", "O(N)", "O(H)"],
    ["349", "349_Recover_BST", "Hard", "Inorder Traversal", "Completed", "O(N)", "O(H)"],
    ["350", "350_Largest_BST_in_Binary_Tree", "Hard", "Postorder DFS", "Completed", "O(N)", "O(H)"]
]

def main():
    filepath = os.path.join(".", "DSA-Knowledge", "Binary_Search_Trees", "tracker.csv")
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Problem", "Difficulty", "Pattern", "Status", "Time_Complexity", "Space_Complexity"])
        writer.writerows(TRACKER_DATA)
    print(f"Updated {filepath} successfully with comprehensive BST data!")

if __name__ == "__main__":
    main()
