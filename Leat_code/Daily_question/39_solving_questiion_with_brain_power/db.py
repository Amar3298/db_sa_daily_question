class Solution:
    def mostPoints(self, questions):
        res = []
        for i in range(len(questions)):
            ta = []
            for j in range(i,len(questions),3):
                ta.append(questions[j][0])
            ta_res = sum(ta)
            res.append(ta_res)
        
        return(max(res))