class Solution:
    def twoSum(self, nums, target):
        searchTable = {}
        for index, val in enumerate(nums):
            valNeeded = target - val
            if valNeeded in searchTable:
                return [searchTable[valNeeded], index]
            else:
                searchTable[val] = index
        return []


def main():
    print(Solution().twoSum([2,7,11,15], 9))

if __name__ == "__main__":
    main()