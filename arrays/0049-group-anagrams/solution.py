class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for i in range(len(strs)):
            arr = [0 for _ in range(1, 27)]
            for j in range(len(strs[i])):
                pos = ord(strs[i][j]) - ord('a')
                arr[pos] += 1
            key = tuple(arr)

            lookup[key] = lookup.get(key, [])
            lookup[key].append(strs[i])
            
        return list(lookup.values())
