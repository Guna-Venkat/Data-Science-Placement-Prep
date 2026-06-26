import csv
import os

TRACKER_DATA = [
    ["102", "102_Search_X_in_sorted_array", "Easy", "Basic BS", "Completed", "O(log N)", "O(1)"],
    ["103", "103_Lower_Bound", "Easy", "Lower Bound", "Completed", "O(log N)", "O(1)"],
    ["104", "104_Upper_Bound", "Easy", "Upper Bound", "Completed", "O(log N)", "O(1)"],
    ["105", "105_Search_insert_position", "Easy", "Lower Bound", "Completed", "O(log N)", "O(1)"],
    ["106", "106_Floor_and_Ceil_in_Sorted_Array", "Easy", "Lower/Upper Bound", "Completed", "O(log N)", "O(1)"],
    ["107", "107_First_and_last_occurrence", "Medium", "First/Last Occur", "Completed", "O(log N)", "O(1)"],
    ["108", "108_Count_Occurrences_in_a_Sorted_Array", "Easy", "Occur Count", "Completed", "O(log N)", "O(1)"],
    ["109", "109_Search_in_rotated_sorted_array_I", "Medium", "Rotated Sorted Search", "Completed", "O(log N)", "O(1)"],
    ["110", "110_Search_in_rotated_sorted_array_II", "Medium", "Rotated Sorted Search", "Completed", "O(N)", "O(1)"],
    ["111", "111_Find_minimum_in_Rotated_Sorted_Array", "Medium", "Rotated Sorted Search", "Completed", "O(log N)", "O(1)"],
    ["112", "112_Find_out_how_many_times_the_array_is_rotated", "Easy", "Rotated Sorted Search", "Completed", "O(log N)", "O(1)"],
    ["113", "113_Single_element_in_a_Sorted_Array", "Medium", "Index Parity Search", "Completed", "O(log N)", "O(1)"],
    ["114", "114_Find_peak_element", "Medium", "Peak Search", "Completed", "O(log N)", "O(1)"],
    ["115", "115_Find_square_root_of_a_number", "Easy", "Root Search", "Completed", "O(log N)", "O(1)"],
    ["116", "116_Find_Nth_root_of_a_number", "Easy", "Root Search", "Completed", "O(log N)", "O(1)"],
    ["117", "117_Koko_eating_bananas", "Medium", "BS on Answer", "Completed", "O(N log(max))", "O(1)"],
    ["118", "118_Minimum_days_to_make_M_bouquets", "Medium", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["119", "119_Find_the_smallest_divisor", "Medium", "BS on Answer", "Completed", "O(N log(max))", "O(1)"],
    ["120", "120_Capacity_to_Ship_Packages_Within_D_Days", "Medium", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["121", "121_Kth_Missing_Positive_Number", "Easy", "Index Math Search", "Completed", "O(log N)", "O(1)"],
    ["122", "122_Aggressive_Cows", "Hard", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["123", "123_Book_Allocation_Problem", "Hard", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["124", "124_Split_array_largest_sum", "Hard", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["125", "125_Painters_Partition", "Medium", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["126", "126_Minimize_Max_Distance_to_Gas_Station", "Hard", "BS on Answer", "Completed", "O(N log(range))", "O(1)"],
    ["127", "127_Median_of_2_sorted_arrays", "Hard", "Matrix Partition Cut", "Completed", "O(log(min(N,M)))", "O(1)"],
    ["128", "128_Kth_element_of_2_sorted_arrays", "Medium", "Matrix Partition Cut", "Completed", "O(log(min(N,M)))", "O(1)"],
    ["129", "129_Find_row_with_maximum_1s", "Easy", "Matrix Corner Search", "Completed", "O(N+M)", "O(1)"],
    ["130", "130_Search_in_a_2D_matrix", "Medium", "2D Flattened Search", "Completed", "O(log(N*M))", "O(1)"],
    ["131", "131_Search_in_2D_matrix_II", "Medium", "Matrix Corner Search", "Completed", "O(N+M)", "O(1)"],
    ["132", "132_Find_Peak_Element_II", "Medium", "Column search with BS", "Completed", "O(M log N)", "O(1)"],
    ["133", "133_Matrix_Median", "Hard", "BS on Answer", "Completed", "O(32 * N log M)", "O(1)"]
]

def main():
    filepath = os.path.join(".", "DSA-Knowledge", "Binary_Search", "tracker.csv")
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Problem", "Difficulty", "Pattern", "Status", "Time_Complexity", "Space_Complexity"])
        writer.writerows(TRACKER_DATA)
    print(f"Updated {filepath} successfully with comprehensive data!")

if __name__ == "__main__":
    main()
