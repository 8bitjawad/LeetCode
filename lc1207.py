class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

        myset = set()

        for key in freq:
            if freq[key] in myset:
                return False
            myset.add(freq[key])
        
        return True
