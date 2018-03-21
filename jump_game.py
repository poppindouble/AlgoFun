# back tracking
# def canJump(nums):
#     availableSteps = nums[0]
#     if availableSteps + 1 >= len(nums):
#         return True
#     for i in range(1, availableSteps + 1):
#         if canJump(nums[i:]):
#             return True
#     return False

# def main():
#     print(canJump([2, 3, 1, 1, 4]))
#     print(canJump([3, 2, 1, 0, 4]))


# top down dynamic programming
# this can be thought as optimized backtracking
# from enum import Enum, auto

# class Status(Enum):
#     GOOD = auto()
#     BAD = auto()
#     UNKNOWN = auto()

# flags = []

# def canJump(nums):
#     global flags 
#     flags = [Status.UNKNOWN for i in range(len(nums))]
#     flags[-1] = Status.GOOD
#     return help(0, nums[:])

# def help(position, nums):
#     global flags

#     if flags[position] != Status.UNKNOWN:
#         return True if flags[position] == Status.GOOD else False

#     furtestJump = min(len(nums) - 1, position + nums[position])
#     for i in range(position + 1, furtestJump + 1):
#         if help(i, nums):
#             flags[position] = Status.GOOD
#             return True

#     flags[position] = Status.BAD
#     return False


# bottom up
# from enum import Enum, auto

# class Status(Enum):
#     GOOD = auto()
#     BAD = auto()
#     UNKNOWN = auto()

# flags = []

# def canJump(nums):
#     global flags
#     flags = [Status.UNKNOWN for x in range(len(nums))]
#     flags[-1] = Status.GOOD
    
#     for i in range(len(nums) - 2, -1, -1):
#         furtestJump = min(i + nums[i], len(nums) - 1)
#         for j in range(i + 1, furtestJump + 1):
#             if flags[j] == Status.GOOD:
#                 flags[i] = Status.GOOD
#                 break

#     return flags[0] == Status.GOOD


# Greedy

def canJump(nums):
    leftMostGoodIndex = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= leftMostGoodIndex:
            leftMostGoodIndex = i
    return leftMostGoodIndex == 0

def main():
    global flags
    # print(canJump([2, 3, 1, 1, 4]))
    # print(canJump([3, 2, 1, 0, 4]))
    # print(canJump([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(canJump([9, 4, 2, 1, 0, 2, 0]))

if __name__ == "__main__":
    main()
