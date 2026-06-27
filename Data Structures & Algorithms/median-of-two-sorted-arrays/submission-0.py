class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        
        m = len(nums1)
        n = len(nums2)
        left = (m+n+1)//2

        lo = 0
        hi = m

        while lo<=hi:
            mid1 = (lo+hi)//2
            mid2 = left - mid1

            l1 = nums1[mid1-1] if mid1>0 else -1e9
            l2 = nums2[mid2-1] if mid2>0 else -1e9
            r1 = nums1[mid1] if mid1<m else 1e9
            r2 = nums2[mid2] if mid2<n else 1e9

            if l1>r2:
                hi = mid1-1
            elif l2>r1:
                lo = mid1+1
            elif l1<=r1 and l2<=r2:
                if (m+n)%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
                    
 
        return 0.0

