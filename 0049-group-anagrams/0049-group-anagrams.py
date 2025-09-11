class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for w in strs:
            key = ''.join(sorted(w))
            groups[key].append(w)
        return list(groups.values())
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)

#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] +=1
#             res[tuple(count)].append(s)
#         return list(res.values())
