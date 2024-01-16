def search_insert(nums, target):
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)

# Example usage:
sorted_array = [1, 3, 5, 6]
target_value = 5
result = search_insert(sorted_array, target_value)