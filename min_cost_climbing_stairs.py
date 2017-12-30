"""
let's define an array, result, result[i] represent 
the minimum cost to GET OVER i,
result[4] means the minimum value to go over 4, which means to reach stair 5
result[5] means the minimum value to go over 5, which means to reach stair 6
so result[i] = min(result[i-2] + cost[i-1], result[i-1] + cost[i])
but this method should start from index 3
becuase [1,0,1]
the minimum value should be 0, but my answer will be 1
the reason is because if index == 2, we still not considering
both situations of walking 1 step and 2 step from the begining
(noticed that player can start from index 1).
so we set the result[2] = min(cost[0] + cost[2], cost[1]).
then we start from the index 3.

solution2:
define result[i] as the minimum cost to include ith stair(cost[i])
so
result[i] = min(result[i-1], result[i-2]) + cost[i]
at the end we just need to return
min(result[-1], result[-2])
"""

class Solution:
	# def minCostClimbingStairs(self, cost):
	# 	if len(cost) == 2:
	# 		return max(cost[0], cost[1])
	# 	result = [0] * len(cost)
	# 	result[0] = cost[0]
	# 	result[1] = min(cost[0], cost[1])
	# 	result[2] = min(cost[0] + cost[2], cost[1])
	# 	for i in range(3, len(cost)):
	# 		result[i] = min(result[i-2] + cost[i-1], result[i-1] + cost[i])
	# 	print(result)
	# 	return result[-1]

	def minCostClimbingStairs(self, cost):
		result = [0] * len(cost)
		result[0] = cost[0]
		result[1] = cost[1]
		for i in range(2, len(cost)):
			result[i] = min(result[i-2], result[i-1]) + cost[i]
		return min(result[-1], result[-2])

def main():
	print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

if __name__ == "__main__":
	main()