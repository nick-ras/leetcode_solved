import os

#leetcode problem with my own implementation (https://leetcode.com/problems/number-of-islands)

class Solution(object):

# checks in all directions for 1's and changes them to 0's
	def recursive_check(self, grid, count_row, count_col, rows, columns):
		# print(i, j, rows, columns)
		if (count_row < 0 or count_row >= rows):
			return
		if (count_col < 0 or count_col >= columns):
			return
		if (grid[count_row][count_col] == '0'):
			return
		
		grid[count_row][count_col] = '0'
		
		Solution.recursive_check(self, grid, count_row - 1, count_col, rows, columns)
		Solution.recursive_check(self, grid, count_row + 1, count_col, rows, columns)
		Solution.recursive_check(self, grid, count_row, count_col - 1, rows, columns)
		Solution.recursive_check(self, grid, count_row, count_col + 1, rows, columns)

# finds number of isldan "1's" for a given grid
	def numIslands(self, grid):
		self.grid = grid
		rows = len(grid)
		columns = len(grid[0])
		#grid = [[int(letter) for letter in x] for x in grid]
		islands = 0
		for count_row, i in enumerate(grid):
			for count_col, j in enumerate(i):
				if (j == '1'):
					islands = islands + 1
					Solution.recursive_check(self, grid, count_row, count_col, rows, columns)
		print(islands)

grid = [
  ["1","0","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

obj = Solution()
obj.numIslands(grid)
