class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            z = 0
            for k in nums:
                if i == k:
                    z += 1
                    continue
                else:
                    continue
            if z > 1:
                answer = True
                break
            else:
                continue

        if z <= 1:
            answer = False
        
        return(answer)
