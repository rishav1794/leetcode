class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        lookup = {}

        for i in range(len(nums1)):
            lookup[nums1[i]] = lookup.get(nums1[i], 0) + 1
        
        for i in range(len(nums2)):
            if nums2[i] in lookup and lookup[nums2[i]] > 0:
                result.append(nums2[i])
                lookup[nums2[i]] -= 1
        return result
