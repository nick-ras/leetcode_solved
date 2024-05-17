from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        for _ in range(k):
            cheapest = costs[0]
            worker = 0
            if len(costs) < candidates:
                candidates = len(costs)
            for i in range(candidates):
                if costs[i] < costs[worker]:
                    worker = i
            print("list", costs, "cand", candidates, "chosen: ", costs[worker])
            total += costs[worker]
            del costs[worker]
        return total

        


sol = Solution()
print(sol.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2))