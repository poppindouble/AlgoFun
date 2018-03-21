def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[mid] > target and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[right]:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    print(left, right)
    return -1


def main():
    print(search([15,22,2,5,9,10,11], 5))
    print(search([17, 4], 5))

if __name__ == "__main__":
    main()