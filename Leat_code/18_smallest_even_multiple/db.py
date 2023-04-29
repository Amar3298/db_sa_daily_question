class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        it = 2
        while(1):
            if(it%n==0 and it%2==0):
                return(it)
                break
            else:
                it += 1