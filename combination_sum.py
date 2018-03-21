def combinationSum(candidates, target):
    temp = []
    res = []
    for index, candidate in enumerate(candidates):
        if target - candidate == 0:
            res += [[candidate]]
        elif target - candidate > 0:
            temp = combinationSum(candidates[index:], target - candidate)
            res += list(map(lambda x: [candidate] + x, temp))
    return res

def main():
    print(combinationSum([2,3,6,7], 7))

if __name__ == "__main__":
    main()