def merge_sort(arr):
    """
    Merge Sort algorithm.
    Time Complexity: O(n log n) (Θ(n log n) for best/average/worst case)
    Space Complexity: O(n) due to temporary arrays used in merging.
    Stable and deterministic sorting algorithm.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge step: O(n)
    i = j = 0
    result = []
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

# Example usage:
data = [5, 2, 9, 1, 5, 6, 7, 3]
print(merge_sort(data))
