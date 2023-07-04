class Solution:
    def singleNumber(self, nums):
        dict1 = {}
        for i in nums:
            if(i not in dict1.keys()):
                dict1[i] = 1
            else:
                dict1[i] += 1 
        for key,value in dict1.items():
            if(value==1):
                return key