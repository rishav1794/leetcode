class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ## --------------------------- Solution 1 ----------------------------
    
      # lookup = {}
        
        # for i in range(len(nums1)):
        #     if nums1[i] in lookup:
        #         continue
        #     lookup[nums1[i]] = 1
        
        # for i in range(len(nums2)):
        #     if nums2[i] in lookup:
        #         value = lookup[nums2[i]]
        #         if value == 2:
        #             continue
        #         if value < 2:
        #             lookup[nums2[i]] += 1
        # res = []
        # for key, value in lookup.items():
        #     if value == 2:
        #         res.append(key)
        # return res

        
        ## --------------------------- Solution 2 ----------------------------

        # lookup = {}
        # res = []

        # for i in range(len(nums1)):
        #     if nums1[i] in lookup:
        #         continue
        #     lookup[nums1[i]] = 1
        
        # for i in range(len(nums2)):
        #     if nums2[i] in lookup and lookup[nums2[i]] == 1:
        #         res.append(nums2[i])
        #     lookup[nums2[i]] = 2
        # return res

        ## --------------------------- Solution 3 ----------------------------

        # lookup = {}
        # res = []

        # for i in range(len(nums1)):
        #     if nums1[i] in lookup:
        #         continue
        #     lookup[nums1[i]] = 1
        
        # for i in range(len(nums2)):
        #     if nums2[i] in lookup and nums2[i] not in res:
        #         res.append(nums2[i])

        # return res

        ## --------------------------- Solution 4 ----------------------------
      
        lookup = {}
        seen = {}
        res = []

        for num in nums1:
            lookup[num] = 1

        for num in nums2:
            if num in lookup and num not in seen:
                res.append(num)
                seen[num] = 1
        return res
      
