def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

nums = [3, 2, 2, 3, 4, 5, 2]
val = 2
result = removeElement(nums, val)

print("Modified Array:", nums)  # Display the modified array.
print("New Length:", result)  # Display the new length.