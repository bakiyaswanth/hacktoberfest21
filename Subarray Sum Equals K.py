class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N, cumv, count = len(nums), 0, 0
        hashmap = {0: 1}
        for i in range(N):
            cumv += nums[i]
            if cumv-k in hashmap:
                count += hashmap[cumv-k]
            if cumv not in hashmap:
                hashmap[cumv] = 0
            hashmap[cumv] += 1
        return count
