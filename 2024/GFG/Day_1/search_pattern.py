class Solution:
    def search(self, pat, txt):
        # code here
        resi = []
        len1 = len(txt)
        for i in range(len1):
          if(txt[i]==pat[0] and txt[i:i+len(pat)] == pat):
            resi.append(i+1)
        if(len(resi)==0):
            return [-1]
        else:
            return resi
        
        