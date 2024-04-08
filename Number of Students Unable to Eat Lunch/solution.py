class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches and sandwiches[0] in students:
            s = students.pop(0)
            if s is sandwiches[0]:
                sandwiches.pop(0)
            else:
                students.append(s)
        return len(students)
