def spiralOrder(matrix):
    result = []
    width, height = len(matrix[0]), len(matrix)
    startX, startY = 0, 0

    while width > 0 and height > 0:
        result += help(matrix, startX, startY, width, height)
        startX += 1
        startY += 1
        width -= 2
        height -= 2
    return result

def help(matrix, startX, startY, width, height):
    res = []
    if width == 1:
        res = [x[startX] for x in matrix[startX : startX + height]]
    elif height == 1:
        res = matrix[startX][startY : startY + width]
    else:
        res += matrix[startX][startY : startY + width]
        res += [x[startY + width - 1] for x in matrix[startX + 1 : startX + height - 1]]
        res += matrix[startY + height - 1][startX : startX + width][::-1]
        res += [x[startY] for x in matrix[startX + 1 : startX + height - 1]][::-1]
    return res

def main():
    print(spiralOrder([[1,2,3],[12,13,4],[11,14,5],[10,15,6],[9,8,7]]))
    print(spiralOrder([[1,2,3]]))
    print(spiralOrder([[1,2,3],[12,13,4],[11,14,5]]))
    print(spiralOrder([[1,2,3],[12,13,4]]))

if __name__ == "__main__":
    main()