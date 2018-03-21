def merge_interval(lists):
    lists.sort(key=lambda x: x[0])
    res = []
    for interval in lists:
        if not res:
            res.append(interval)
        else:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
    return res
        

print(merge_interval([[8,10], [1,3], [15,18], [2,6]]))
