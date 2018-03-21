# def findPeakElement(nums):
#     size = len(nums)
#     for i in range(1, size - 1):
#         if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
#             return i
#     return [0, size - 1][nums[0] < nums[size - 1]]

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(findPeakElement([1,2,3,-2,4,5,-1,-2,-3,-4,10]))
print(findPeakElement([1,2,3]))
print(findPeakElement([3,2,1]))
print(findPeakElement([3,2,1,2,3]))