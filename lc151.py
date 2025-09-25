class Solution:
    def reverseWords(self, s: str) -> str:

        cleaned = s.split() #["hello", "world"]
        front=0
        back=len(cleaned)-1

        while(front <= back):
            cleaned[front],cleaned[back]=cleaned[back],cleaned[front]
            front+=1
            back-=1

        result= " ".join(cleaned)

        return result
