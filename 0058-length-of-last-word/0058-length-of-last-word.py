class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) -1, 0 #index of last character, length set to 0
        
        #eliminating white spaces
        #start from end of sentence (decrement)
        
        while s[i] == " ":
            i-=1
        while i>=0 and s[i] != " ": #counting the characters , string index is not whitespace
            length +=1
            i -=1 #increment pointer
        return length
        
        
        
        