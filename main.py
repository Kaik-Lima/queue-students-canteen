class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        self.students = students
        self.sandwiches = sandwiches
        # Se o comprimento dos dados forem diferentes ou maiores que 100
        if len(self.students) != len(self.sandwiches) or len(self.students) > 100: return None
        # Se os dados dos sanduíches forem diferentes de 0 e 1.
        for i in self.students:
            if i != 0 and i != 1: return None
        # Enquanto houver alunos na fila.
        for i in self.sandwiches:
            if i != 0 and i != 1: return None
        # Lógica e Sistema
        while len(self.students) >= 1:
            if self.students[0] == self.sandwiches[0]:
                del self.students[0]
                del self.sandwiches[0]
            else:
                self.students.append(self.students[0])
                del self.students[0]
                # Verificador de loop
                if len(set(self.students)) == 1: break
        # Retorna a quantidade de alunos que restou na fila
        return len(self.students)


queue = Solution()

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
queue.countStudents(students, sandwiches)