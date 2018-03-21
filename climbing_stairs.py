def climbing_stairs(m):
    if m == 1:
        return 1
    if m == 2:
        return 2
    first = 2
    second = 1
    for i in range(3, m + 1):
        cur = first + second
        second = first
        first = cur
    return cur

print(climbing_stairs(6))