class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        newArr = set()
        for num in set1:
            if num in set2:
                newArr.add(num)
        return list(newArr)
