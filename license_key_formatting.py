class Solution:
	# def licenseKeyFormatting(self, S, K):
	# 	temp = "".join(S.split("-"))
	# 	padding = ""
	# 	if len(temp) % K != 0:
	# 		padding = "#" * (K - len(temp) % K)
	# 	temp = padding + temp
	# 	i = 0
	# 	result = []
	# 	while i < len(temp):
	# 		result.append(temp[i:i+K])
	# 		i += K
	# 	print((K - len(temp) % K))
	# 	return "-".join(result).replace("#", "")

	def licenseKeyFormatting(self, S, K):
		S = S.replace('-', '').upper()
		if len(S) % K:
			S = '#' * (K - len(S) % K) + S
		return '-'.join(S[x:x + K] for x in range(0, len(S), K)).replace('#', '')

def main():
	print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))

if __name__ == "__main__":
	main()