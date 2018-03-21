# def permutation(list):
#     result = dfs(list[:], "", [])
#     return result

# def dfs(list, s, res):
#     if not list:
#         res.append(s)
#         return res[:]
#     result = []
#     for index, num in enumerate(list):
#         result += dfs(list[0 : index] + list[index + 1 :], s + str(list[index]), res[:])
#     return result

def permutation(nums):
    if len(nums) == 1:
        return [nums]
    res = []
    for index, num in enumerate(nums):
        temp = permutation(nums[0 : index] + nums[index + 1 :])
        res += list(map(lambda x: [num] + x, temp))
    return res

def main():
    print(permutation([1,2,3]))

if __name__ == "__main__":
    main()