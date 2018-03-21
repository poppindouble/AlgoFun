def fractionToDecimal(numerator, denominator):
    negativeFlag = numerator * denominator < 0
    numList = []
    loopStr = None
    numerator = abs(numerator)
    denominator = abs(denominator)
    cnt = 0
    loopDict = {}
    while True:
        numList.append(str(numerator // denominator))
        cnt += 1
        numerator = 10 * (numerator % denominator)
        if numerator == 0:
            break
        loc = loopDict.get(numerator)
        if loc:
            loopStr = "".join(numList[loc:])
            break
        else:
            loopDict[numerator] = cnt

    ans = numList[0]
    if len(numList) > 1:
        ans += "."
    if loopStr:
        ans += "".join(numList[1 : len(numList) - len(loopStr)]) + "(" + loopStr + ")"
    else:
        ans += "".join(numList[1:])
    if negativeFlag:
        ans = "-" + ans
    return ans


print(fractionToDecimal(1, 6))