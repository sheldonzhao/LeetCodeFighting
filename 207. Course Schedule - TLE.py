class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create graph
        graph = {}
        for edge in prerequisites:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
        # traversal
        self.flag = 0
        for vertex in range(numCourses):
            if self.flag == 1:
                return False

            self.record = {}
            if vertex in graph:
                self.DFS(vertex, graph)

        return True

    def DFS(self, vertex, graph):
        if self.flag == 1:
            return

        self.record[vertex] = 1
        if vertex in graph:
            for v in graph[vertex]:
                if v in self.record:
                    self.flag = 1
                    return
                self.DFS(v, graph)
        del self.record[vertex]

mySolution = Solution()
course_num = 3
prerequisite1 = [[0, 1], [0, 2], [1, 2]]
prerequisite2 = [[0, 2], [1, 2], [2, 0]]
flag1 = mySolution.canFinish(course_num, prerequisite1)
print(flag1)
flag2 = mySolution.canFinish(course_num, prerequisite2)
print(flag2)
