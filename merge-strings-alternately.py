#Link: https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)==0:
            return word2
        elif len(word2)==0:
            return word1
        elif len(word1)==len(word2):
            res=''
            for i in range(len(word1)):
                res+=word1[i]+word2[i]
            return res
        else:
            res=''
            if len(word1)<len(word2):
                for i in range(len(word1)):
                    res+=word1[i]+word2[i]
                res+=word2[len(word1):]
            else:
                for i in range(len(word2)):
                    res+=word1[i]+word2[i]
                res+=word1[len(word2):]
            return res
