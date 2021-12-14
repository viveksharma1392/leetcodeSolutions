# for consider each character as middle of palindrom, now for each character try to find out the length of palindrom
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==0 or len(s)==1):
            return s
        if(len(s)==2):
            if s[0]==s[1]:
                return s
            else:
                return s[:1]
        l=0
        r=0
        opt_l=0
        opt_r=0
        for i in range(0,len(s)):
            
            # odd length case
            l=i
            r= i
            while(l>-1 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            
            if (opt_r-opt_l)<(r-l):
                opt_r = r
                opt_l = l
        
        
            #even legth case 
            l=i
            r=i+1
            while(l>-1 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            
            if (opt_r-opt_l)<(r-l):
                opt_r = r
                opt_l = l
        
        if(opt_r-opt_l==0):
            return s[:1]
        
        #print(opt_l, opt_r)
        
        return s[opt_l+1:opt_r]
            
            
        