class Solution:
    def leastInterval(self, N, K, tasks):
        # Frequency count of each character
        dict1 = {}
        for i in tasks:
            if(i not in dict1.keys()):
                dict1[i] = 1
            else:
                dict1[i] += 1 
        
        # Highest Frequency 
        highest_frequency = max(list(dict1.values()))
        no_of_highest_frequency = 0

        # No of Highest Frequency
        for i in list(dict1.values()):
            if(i==highest_frequency):
                no_of_highest_frequency += 1

        # sometime might be case we have Suspended time to 0 in that case we will return the lenght of tasks
        # (highest_frequency - 1) * (Suspended time period + 1) + no_of_frequency_having_highest_frequency_count
        res = max(len(tasks),(highest_frequency - 1) * (K + 1) + no_of_highest_frequency)
        return res
"""
N = 6
K = 2
task[ ] = {'A', 'A', 'A', 'B', 'B', 'B'}
"""
        
obj = Solution()
res = obj.leastInterval(6,2,['A', 'A', 'A', 'B', 'B', 'B'])
print(res)