class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for string in strs:
            encoded_string+=str(len(string))+"#"+string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            j+=1
            word=s[j:j+length]
            result.append(word)
            i=j+length
        
        return result
