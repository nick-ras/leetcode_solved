
class Solution:
	def removeElement(self,) -> int:
		nums = [0,1,2,2,3,0,4,2]
	  
		val = 2
		for index, x in nums:
				if nums[index] == val:
						del nums[index]
				else:
						index += 1

		return len(nums)

sol = Solution()
print(sol.removeElement())
