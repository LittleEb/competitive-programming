class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            y=0
            for j in nums2:
                y+=1 
                if i == j:
                    for z in nums2[y:]:
                        if y < len(nums2):
                            if nums2[y] > j:
                                ans += [(nums2[y])]
                                break
                            else:
                                y+=1
                                continue
                        else:
                            ans += [-1]
                    else:
                        ans += [-1]
        return (ans)
