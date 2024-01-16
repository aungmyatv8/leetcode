def removeDuplicates(nums):
	print(sorted(set(nums)))
	nums[:] = sorted(set(nums))
	print(nums)
	return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))