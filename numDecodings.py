def numDecodings(s):
    if s == "" or s == "0":
        return 0
    dp = [1, 1]
    for index in range(2, len(s) + 1):
        if 10 <= int(s[index - 2 : index]) <= 26 and s[index - 1] != "0":
            dp.append(dp[index - 1] + dp[index - 2])
        elif s[index - 2 : index] == "10" or s[index - 2 : index] == "20":
            dp.append(dp[index - 2])
        elif s[index - 1] != "0":
            dp.append(dp[index - 1])
        else:
            return 0
    return dp[len(s)]

print(numDecodings("01"))