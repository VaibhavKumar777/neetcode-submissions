class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)
        new_list = []
        for word in strs:
            wor = "".join(sorted(word))
            groups[wor].append(word)
        for val in groups.values():
            new_list.append(val)
        return new_list