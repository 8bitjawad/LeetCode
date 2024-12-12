class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        max_gift=0
                
        while k>0:
            max_gift=max(gifts)
            index=gifts.index(max_gift)
            gifts[index]= math.floor(math.sqrt(max_gift))

            k-=1
       
        return sum(gifts)