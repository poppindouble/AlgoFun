def maxProduct(nums):
    if len(nums) < 1:
        return 0
    tempMax = nums[0]
    tempMin = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        a = max(nums[i], tempMax * nums[i], tempMin * nums[i])
        b = min(nums[i], tempMax * nums[i], tempMin * nums[i])
        tempMax = a
        tempMin = b
        print(tempMax, tempMin)
        result = max(result, tempMax)
    return result

print(maxProduct([2, 3, -2, -1, 10, -9]))