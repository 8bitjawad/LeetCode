class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitude = [0] * (n+1)
        i=0

        for i in range(n):
            altitude[i+1] = altitude[i] + gain[i]

        max_alt = max(altitude)

        return max_alt

