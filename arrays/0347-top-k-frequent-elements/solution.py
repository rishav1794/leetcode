class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        ret = []

        for i in range(len(nums)):
            lookup[nums[i]] = lookup.get(nums[i], 0) + 1

        res = [[] for _ in range(len(nums)+1)]

        for num, frequency in lookup.items():
            res[frequency].append(num)

        for i in range(len(res)-1, -1, -1):
            if res[i]:
                for num in res[i]:
                    ret.append(num)
            if len(ret) == k:
                return ret
