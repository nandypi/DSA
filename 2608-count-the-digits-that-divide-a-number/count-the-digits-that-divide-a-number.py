class Solution:
    def countDigits(self, num: int) -> int:
        count = 0; cnum = num
        while cnum>0:
            ld = cnum % 10
            if ld != 0 and num % ld == 0:
                count += 1
            cnum = cnum//10
        return count
