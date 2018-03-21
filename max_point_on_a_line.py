class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(points):
    length = len(points)
    if length < 3:
        return length
    maxNum = -1
    for i in range(length):
        temp = {}
        temp['inf'] = 0
        samePoint = 1
        for j in range(length):
            if j == i:
                continue
            if points[i].x == points[j].x and points[i].y != points[j].y:
                temp['inf'] += 1
            elif points[i].x != points[j].x:
                k = (points[i].y - points[j].y) / (points[i].x - points[j].x)
                if k not in temp:
                    temp[k] = 1
                else:
                    temp[k] += 1
            else:
                samePoint += 1
        maxNum = max(maxNum, max(temp.values()) + samePoint)
    return maxNum

point0 = Point(0, 0)
point1 = Point(94911151, 94911150)
point2 = Point(94911152, 94911151)
# point3 = Point(2, 2)
# point4 = Point(5, 5)
# point5 = Point(1, 0)
# point6 = Point(0, 1)
# point7 = Point(4, 2)

# points = [point0,point1,point2,point3,point4,point5,point6,point7]
points = [point0,point1,point2]
print(maxPoints(points))