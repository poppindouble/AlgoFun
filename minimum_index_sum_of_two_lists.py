class Solution:
	def findRestaurant(self, list1, list2):
		myDict = {}
		for index, place in enumerate(list1):
			myDict[place] = index
		miniIndex = len(list1) + len(list2)
		result = []
		for index, place in enumerate(list2):
			if place not in myDict:
				continue
			temp = index + myDict[place]
			if temp <= miniIndex:
				if temp < miniIndex:
					miniIndex = temp
					result.clear()
				result.append(place)
		return result


def main():
	print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))

if __name__ == "__main__":
	main()