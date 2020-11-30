class StudentGrades:
    def __init__(self,studentID, lastName='', firstName='', grades = [[],[],[]]):
        self.studentID = studentID
        self.lastName = lastName
        self.firstName = firstName
        self.grades = grades
    def setLastName(self, lastName):
        self.lastName = lastName
    def setfirstName(self, firstName):
        self.firstName = firstName
    def getStudenID(self):
        return self.studentID
    def getLastName(self):
        return self.lastName
    def getFirstName(self):
        return self.firstName
    def getGrades(self):
        return self.grades
    def addGrades(self,scores,other):
        if other == 'Q':
            self.grades[0].append(scores)
        if other == 'H':
            self.grades[1].append(scores)
        if other == 'L':
            self.grades[2].append(scores)
    def averageGrades(self):
        sum_Q = 0
        sum_H = 0
        sum_L = 0
        avg_Q = 0
        avg_H = 0
        avg_L = 0
        if len(self.grades[0]) == 0:
            avg_Q = 0
        else:
            for i in self.grades[0]:
                sum_Q += i
            avg_Q = round(sum_Q/len(self.grades[0]))
        if len(grades[1]) == 0:
            avg_H = 0
        else:
            for j in self.grades[1]:
                sum_H += j
            avg_H = round(sum_H/len(self.grades[1]))
        if len(self.grades[2]) == 0:
            avg_L = 0
        else:
            for k in self.grades[2]:
                sum_L += k
            avg_L = round(sum_L/len(self.grades[2]))
        newlist = [avg_Q, avg_H,avg_L]
        return newlist
    def __str__(self):
        res=str('ID: '+ str(self.studentID) +
               '\nGrades: '+str(self.grades) +
               '\nAverages: '+ str(self.averageGrades()))
        return res

if __name__ == '__main__':
    studentID = int(input('studentID: '))
    lastName = str(input('lastName: '))
    firstName = str(input('firstName: '))
    quiz = list(map(int,input('quiz grades: ').split(',')))
    homework = list(map(int,input('homework grades: ').split(',')))
    lab = list(map(int,input('lab grades: ').split(',')))
    grades=[quiz,homework,lab]
    student=StudentGrades(studentID,lastName,firstName,grades)
    print(student)
