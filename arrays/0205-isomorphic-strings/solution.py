class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup_s = {}
        lookup_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            source = s[i]
            target = t[i]

            if source in lookup_s:
                if lookup_s[source] != target:
                    return False
            
            if target in lookup_t:
                if lookup_t[target] != source:
                    return False
            
            lookup_s[source] = target
            lookup_t[target] = source
        return True
