class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        base = 2
        while True:
            re = self.numberToBase(num, base)
            if re is False:
                base += 1
            else:
                return str(base)

    def numberToBase(self,n, b):
        #digits = []
        while n:
            reminder = int(n % b)
            if reminder != 1:
                return False
            #digits.append(reminder)
            n //= b
        return True


mySolution = Solution()
base = mySolution.smallestGoodBase(677)
print(base)
