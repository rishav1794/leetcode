class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lookup = {}
        if len(magazine) < len(ransomNote):
            return False

        for s in magazine:
            lookup[s] = lookup.get(s, 0) + 1
        
        for s in ransomNote:
            if s in lookup and lookup[s] > 0:
                lookup[s] -= 1
            else:
                return False
        return True
