def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while nums[i] > 0 and nums[i] <= n \
            and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1
            

def main():
    firstMissingPositive([3,4,-1,1])

if __name__ == "__main__":
    main()