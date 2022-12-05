from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        sort_nums3 = sorted(nums3)
        if len(sort_nums3) % 2 == 0:
            return (sort_nums3[len(sort_nums3)//2] + sort_nums3[len(sort_nums3)//2-1]) / 2
        else:
            return sort_nums3[len(sort_nums3)//2]