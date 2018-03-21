class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] == -nums[i]:
                        result.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif nums[start] + nums[end] < -nums[i]:
                        while start < end:
                            start += 1
                            if nums[start] != nums[start - 1]:
                                break
                    else:
                        while start < end:
                            end -= 1
                            if nums[end] != nums[end + 1]:
                                break
        return result

def main():
    print(Solution().threeSum([-1,0,1,2,-1,-4]))

if __name__ == "__main__":
    main()