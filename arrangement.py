
def main(num):
	array = [i for i in range(1,10)]
	print(search(array, num))

def search(array, num):
	final = []
	for i in array:
		if num == 0:
			final.append([i])
			continue
		newList = list(filter(lambda x: x != i, array))
		temp = search(newList, num - 1)
		result = list(map(lambda x: [i] + x, temp))
		final = final + result
	return final

if __name__ == "__main__":
	main(5)