# def uniquePaths(m, n):
#     return help([0, 0], m, n, "")

# def help(startPoint, m, n, temp):
#     res = []
#     down = []
#     right = []
#     if startPoint[0] == m -1 and startPoint[1] == n - 1:
#         res.append(temp)
#         return res[:]
#     if startPoint[0] < m - 1:
#         newStartPoint = [startPoint[0] + 1, startPoint[1]]
#         down = help(newStartPoint, m, n, temp + "down ")
#     if startPoint[1] < n - 1:
#         newStartPoint = [startPoint[0], startPoint[1] + 1]
#         right = help(newStartPoint, m, n, temp + "right ")
#     return down + right


# time limited exceed
# def uniquePaths(m, n):
#     return help([0, 0], m, n)

# def help(startPoint, m, n):
#     down, right = 0, 0
#     if startPoint[0] == m - 1 and startPoint[1] == n - 1:
#         return 1
#     if startPoint[0] < m - 1:
#         newStartPoint = [startPoint[0] + 1, startPoint[1]]
#         down = help(newStartPoint, m, n)
#     if startPoint[1] < n - 1:
#         newStartPoint = [startPoint[0], startPoint[1] + 1]
#         right = help(newStartPoint, m, n)
#     return down + right

def uniquePaths(m, n):
        if m == 1 and n == 1:
            result = [[1]]
        elif m == 1:
            result = [[1 for i in range(n)]]
        elif n == 1:
            result = [[1] for i in range(m)]
        else:
            result = [[1 for i in range(n)] for i in range(m)]
            for i in range(n):
                result[0][i] = 1
            for j in range(m):
                result[j][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[m - 1][n - 1]


print(uniquePaths(1, 2))