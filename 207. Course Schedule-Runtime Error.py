class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #  argument check
        if numCourses is None or prerequisites is None:
            return
        if numCourses and prerequisites == [[]]:
            return True

        # DFS for every pairs in prerequisites
        len_pre = len(prerequisites)
        self.flag = True
        for i in range(len_pre):
            circle_num = prerequisites[i][0]
            self.DFS(prerequisites, i, circle_num)

        return self.flag

    def DFS(self, prerequisites, pos, circle_num):
        for i in prerequisites[:pos] + prerequisites[pos + 1:]:
            if prerequisites[pos][1] == i[0]:
                if i[1] == circle_num:
                    self.flag = False
                    return
                else:
                    self.DFS(prerequisites, prerequisites.index(i), circle_num)


mySolution = Solution()
course_num = 3
prerequisite1 = [[1, 0], [0, 1]]
prerequisite2 = [[0, 2], [1, 2], [2, 0]]
flag = mySolution.canFinish(course_num, prerequisite2)
print(flag)
