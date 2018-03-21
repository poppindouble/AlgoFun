class Solution:
    def nextPermutation(self, nums):
        if len(nums) <= 1:
            return nums
        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break
        if partition == -1:
            return nums.reverse()

        for i in range(len(nums) - 1, partition, -1):
            if nums[i] > nums[partition]:
                nums[i], nums[partition] = nums[partition], nums[i]
                break

        left = partition + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

def main():
    print(Solution().nextPermutation([5,3,2,1,6,4]))

if __name__ == "__main__":
    main()