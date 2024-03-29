#git add .\unique_paths.py ; git commit -m "h" ; git push
class Solution():

	def recursive(self, m, n, hori, vert):
		if (vert == m or hori == n):
			return 1
		return Solution.recursive(self, m, n, hori + 1, vert) + Solution.recursive(self, m, n, hori, vert + 1)

	def uniquePaths(self, m, n):
		res = Solution.recursive(self, m, n, 1, 1)
		return res

