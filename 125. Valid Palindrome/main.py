class Solution:
    def isPalindrome(self, s: str) -> bool:
        #space
        #s=s.strip()
        #ignore cases
        s=s.lower()
        #special character
        i=0
        processing=''
        while i < len(s):
            if s[i].isalnum():
                processing += s[i]
            i += 1        
            
        if (len(processing)%2) == 1:
            begin1 = 0
            end1 = len(processing)//2
            begin2 = len(processing)//2 + 1
            end2 = len(processing)
        else:
            begin1 = 0
            end1 = len(processing)//2
            begin2 = len(processing)//2
            end2 = len(processing)

        temp1=processing[begin1:end1]
        temp2=processing[begin2:end2]
        
        if temp1=="".join(reversed(temp2)):
            return True
        else:
            return False