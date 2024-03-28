from typing import List
from itertools import permutations
import collections


import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        results = []
        unique = []
        substr_len = len(words[0]) * len(words)
        word_count = len(words)
        word_len = len(words[0])
        for i in range (0, len(s) - substr_len + 1):
            substr = s[i:i+substr_len]
            if s[i:i + word_len] or s[i + word_len:i + word_len] not in words:
                continue
            substr_results = collections.Counter([substr[j:j + word_len] for j in range(0, substr_len, word_len)])
            #print(substr_results)
            success = True
            for word, count in substr_results.items():
                if words.count(word) != count:
                    success = False
            if success == True:
                results.append(i)
        return results

sol = Solution()
print("[2] -->")
print(sol.findSubstring("ggabefcder", ["ab","cd","ef"]))
print(" [0, 9] ->")
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(" [8] -->")
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
      
    # def findSubstring(self, s: str, words: List[str]) -> str:
    #     #got to get it shows indexes
    #     results = []
    #     word_permutations = [''.join(p) for p in permutations(words)]
    #     print(word_permutations)
    #     for perm in word_permutations:
    #         print(perm + "   " + s)
    #         if perm in s:
    #             start_index = s.find(perm)
    #             while start_index != -1:
    #                 results.append(start_index)
    #                 start_index = s.find(perm, start_index + 1)
    #             return results
    #     return None