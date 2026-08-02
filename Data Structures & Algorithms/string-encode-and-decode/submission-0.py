class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded+=str(length)+"#"+word
        return encoded
    def decode(self, s: str) -> List[str]:
        length = 0
        decoded = []
        
        i = 0
        while i<len(s):
            final_word = ""
            length = ""
            while s[i]!='#':
                length+=s[i]
                i+=1
            length = int(length)
            i += 1
            final_word = s[i:i+length]
            i += length
            decoded.append(final_word)
        return decoded