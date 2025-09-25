class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0  # position to write
        read = 0

        while read < n:
            char = chars[read]
            count = 0
            # count consecutive same chars
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # write the character
            chars[write] = char
            write += 1

            # write the count if greater than 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
