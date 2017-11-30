'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
'''
'''
    self.DFS(num, 0, -1, s)
    def DFS(self, num, pos, index, s):
        if pos == num:
            print(s)
            self.res.append(s)
            return
        for i in range(index + 1, 4):
            s_copy = deepcopy(s)
            s_copy[i] = 1
            self.DFS(num, pos + 1, i, s_copy)
'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]
