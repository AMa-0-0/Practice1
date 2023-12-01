def merge_sort(lst):
    if len(lst) <= 1:
        return lst  # A list of zero or one elements is already sorted.
    if len(lst) == 2:
        return sorted(lst)  # Sort a list of two elements trivially.
    
    # Split the list into two roughly equal halves
    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged_list = []
    left_index, right_index = 0, 0
    
    # Merge the two lists into a sorted one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
    
    # If there are remaining elements in left or right, append them
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    
    return merged_list

# Example usage:
unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = merge_sort(unsorted_list)
print("Sorted list:", sorted_list)
