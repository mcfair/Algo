class Solution:
	def numDistinct(self, S, T):
		matches = [1] + [0] * len(T)
        
		for i in range(len(S)):
			for j in reversed(range(len(T))):
				if T[j] == S[i]:
					matches[j+1] += matches[j]
		return matches[-1]
