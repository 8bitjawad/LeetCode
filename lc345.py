class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        front, back = 0, len(s) - 1

        while front < back:
            if s[front] not in vowels:
                front += 1
                continue
            if s[back] not in vowels:
                back -= 1
                continue

            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1

        return "".join(s)
