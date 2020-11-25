class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        max_students = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                max_students += 1
        return max_students
