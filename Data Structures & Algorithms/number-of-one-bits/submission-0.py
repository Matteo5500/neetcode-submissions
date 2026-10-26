class Solution:
    def hammingWeight(self, n: int) -> int:
        binario = bin(n)
        counter = 0
        for digit in binario:
            if digit == "1":
                counter += 1

        return counter
