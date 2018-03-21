def largestRectangleArea(heights):
    maxArea = 0
    heightStack = []
    indexStack = []
    for index, height in enumerate(heights):
        if not heightStack or height > heightStack[-1]:
            heightStack.append(height)
            indexStack.append(index)
        elif height < heightStack[-1]:
            lastIndex = 0
            while heightStack and height < heightStack[-1]:
                lastIndex = indexStack.pop()
                tempArea = heightStack.pop() * (index - lastIndex)
                if tempArea > maxArea:
                    maxArea = tempArea
            heightStack.append(height)
            indexStack.append(lastIndex)

    while heightStack:
        tempArea = (len(heights) - indexStack.pop()) * heightStack.pop()
        if tempArea > maxArea:
            maxArea = tempArea
    return maxArea


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(largestRectangleArea([9, 8, 1]))