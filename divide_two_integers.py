class Solution:
    def divide(self, dividend, divisor):

        isNeg = False
        sum = 0
        counter = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)

        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
            isNeg = True
            if abs(dividend) < abs(divisor):
                return 0

        while a >= b:
            counter = 1
            sum = b
            while sum + sum <= a:
                sum += sum
                counter += counter
            a -= sum
            res += counter

        if isNeg:
            return -res
        return res

def main():
    print(Solution().divide(0, 1))

if __name__ == "__main__":
    main()