def binary_search(arr, target):
    """
    Iterative Binary Search.
    - Precondition: arr must be SORTED.
    Time Complexity: O(log n) (Θ(log n), Ω(1) in the best case if the target is in the middle)
    Space Complexity: O(1) (iterative)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
nums = list(range(0, 100, 2))   # [0, 2, 4, ...]
print(binary_search(nums, 42))  # index of 42 or -1
