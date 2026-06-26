import csv
import os

TRACKER_DATA = [
    ["062", "062_Largest_Element", "Easy", "Array Traversal", "Completed", "O(N)", "O(1)"],
    ["063", "063_Second_Largest_Element", "Easy", "Array Traversal", "Completed", "O(N)", "O(1)"],
    ["064", "064_Check_if_the_Array_is_Sorted_II", "Easy", "Array Traversal", "Completed", "O(N)", "O(1)"],
    ["065", "065_Remove_duplicates_from_Sorted_array", "Easy", "Two Pointers", "Completed", "O(N)", "O(1)"],
    ["066", "066_Left_Rotate_Array_by_One", "Easy", "Array Rotation", "Completed", "O(N)", "O(1)"],
    ["067", "067_Left_Rotate_Array_by_K_Places", "Medium", "Array Rotation / Reversal", "Completed", "O(N)", "O(1)"],
    ["068", "068_Move_Zeros_to_End", "Easy", "Two Pointers", "Completed", "O(N)", "O(1)"],
    ["069", "069_Linear_Search", "Easy", "Linear Search", "Completed", "O(N)", "O(1)"],
    ["070", "070_Union_of_two_sorted_arrays", "Easy", "Two Pointers / Merge", "Completed", "O(N+M)", "O(1)"],
    ["071", "071_Find_missing_number", "Easy", "Math / XOR", "Completed", "O(N)", "O(1)"],
    ["072", "072_Maximum_Consecutive_Ones", "Easy", "Counter", "Completed", "O(N)", "O(1)"],
    ["073", "073_Find_the_number_that_appears_once_and_other_numbers_twice", "Easy", "XOR Bitwise", "Completed", "O(N)", "O(1)"],
    ["074", "074_Longest_subarray_with_given_sum_Kpositives", "Medium", "Sliding Window", "Completed", "O(N)", "O(1)"],
    ["075", "075_Longest_subarray_with_sum_K", "Medium", "Prefix Sum + HashMap", "Completed", "O(N)", "O(N)"],
    ["076", "076_Two_Sum", "Easy", "HashMap Lookup", "Completed", "O(N)", "O(N)"],
    ["077", "077_Sort_an_array_of_0s_1s_and_2s", "Medium", "Dutch National Flag", "Completed", "O(N)", "O(1)"],
    ["078", "078_Majority_Element_I", "Easy", "Boyer-Moore Voting", "Completed", "O(N)", "O(1)"],
    ["079", "079_Kadanes_Algorithm", "Medium", "Kadane's Algorithm", "Completed", "O(N)", "O(1)"],
    ["080", "080_Print_subarray_with_maximum_subarray_sum", "Medium", "Kadane's with Pointers", "Completed", "O(N)", "O(1)"],
    ["081", "081_Stock_Buy_and_Sell", "Easy", "Greedy / Min-Track", "Completed", "O(N)", "O(1)"],
    ["082", "082_Rearrange_array_elements_by_sign", "Medium", "Two Pointers", "Completed", "O(N)", "O(N)"],
    ["083", "083_Next_Permutation", "Medium", "Lexicographical Swap", "Completed", "O(N)", "O(1)"],
    ["084", "084_Leaders_in_an_Array", "Easy", "Scan from Right", "Completed", "O(N)", "O(1)"],
    ["085", "085_Longest_Consecutive_Sequence_in_an_Array", "Medium", "Set / Hashing", "Completed", "O(N)", "O(N)"],
    ["086", "086_Set_Matrix_Zeroes", "Medium", "Matrix Markers", "Completed", "O(N*M)", "O(1)"],
    ["087", "087_Rotate_matrix_by_90_degrees", "Medium", "Transpose & Reverse", "Completed", "O(N^2)", "O(1)"],
    ["088", "088_Print_the_matrix_in_spiral_manner", "Medium", "Boundary Traversal", "Completed", "O(N*M)", "O(1)"],
    ["089", "089_Count_subarrays_with_given_sum", "Medium", "Prefix Sum + HashMap", "Completed", "O(N)", "O(N)"],
    ["090", "090_Pascals_Triangle_I", "Easy", "Dynamic Programming", "Completed", "O(N^2)", "O(N^2)"],
    ["091", "091_Majority_Element_II", "Medium", "Boyer-Moore Voting", "Completed", "O(N)", "O(1)"],
    ["092", "092_3_Sum", "Medium", "Sorting + Two Pointers", "Completed", "O(N^2)", "O(1)"],
    ["093", "093_4_Sum", "Medium", "Sorting + Two Pointers", "Completed", "O(N^3)", "O(1)"],
    ["094", "094_Largest_Subarray_with_Sum_0", "Medium", "Prefix Sum + HashMap", "Completed", "O(N)", "O(N)"],
    ["095", "095_Count_subarrays_with_given_xor_K", "Medium", "Prefix XOR + HashMap", "Completed", "O(N)", "O(N)"],
    ["096", "096_Merge_Overlapping_Subintervals", "Medium", "Sorting + Merge", "Completed", "O(N log N)", "O(N)"],
    ["097", "097_Merge_two_sorted_arrays_without_extra_space", "Hard", "Gap Method / Shell Sort", "Completed", "O((N+M) log(N+M))", "O(1)"],
    ["098", "098_Find_the_repeating_and_missing_number", "Medium", "Math / XOR", "Completed", "O(N)", "O(1)"],
    ["099", "099_Count_Inversions", "Hard", "Divide & Conquer / Merge Sort", "Completed", "O(N log N)", "O(N)"],
    ["100", "100_Reverse_Pairs", "Hard", "Divide & Conquer / Merge Sort", "Completed", "O(N log N)", "O(N)"],
    ["101", "101_Maximum_Product_Subarray_in_an_Array", "Medium", "Prefix/Suffix Products", "Completed", "O(N)", "O(1)"]
]

def main():
    filepath = os.path.join(".", "DSA-Knowledge", "Arrays", "tracker.csv")
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Problem", "Difficulty", "Pattern", "Status", "Time_Complexity", "Space_Complexity"])
        writer.writerows(TRACKER_DATA)
    print(f"Updated {filepath} successfully with comprehensive data!")

if __name__ == "__main__":
    main()
