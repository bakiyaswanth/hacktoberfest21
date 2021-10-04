class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        while(i < n):
            nums1[i + m] = nums2[i]
            i += 1
        nums1.sort()
