from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        used = set()
        for i in range(len(strs)):
            if i in used:
                continue
            used.add(i)
            new = [strs[i]]
            for j in range(i+1,len(strs)):
                if Counter(strs[i]) == Counter(strs[j]):
                    new.append(strs[j])
                    used.add(j)
            new_list.append(new)
        return new_list
