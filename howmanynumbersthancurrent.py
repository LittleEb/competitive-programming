class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            z = 0
            for j in nums:
                if i > j:
                    z+=1
            answer.append(z)
        return(answer)
