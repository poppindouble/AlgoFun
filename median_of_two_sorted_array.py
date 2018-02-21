class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k = len(nums1) + len(nums2)
        if k%2 == 1:
            return self.findKthNumber(nums1, nums2, k//2 + 1) * 1.0
        else:
            return (self.findKthNumber(nums1, nums2, k//2)
                    + self.findKthNumber(nums1, nums2, k//2 + 1)) * 0.5
        

    def findKthNumber(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKthNumber(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        positionA = min(len(nums1), k//2)
        positionB = k - positionA
        if nums1[positionA-1] < nums2[positionB-1]:
            return self.findKthNumber(nums1[positionA:], nums2, positionB)
        else:
            return self.findKthNumber(nums1, nums2[positionB:], positionA)


def main():
    print(Solution().findMedianSortedArrays([2,7,11,15], [1,3,5]))

if __name__ == "__main__":
    main()