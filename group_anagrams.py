def groupAnagrams(strs):
    dict = {}
    for str in strs:
        key = "".join(sorted(str))
        if key not in dict:
            dict[key] = [str]
        else:
            dict[key].append(str)
    return list(dict.values())


def main():
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == "__main__":
    main()