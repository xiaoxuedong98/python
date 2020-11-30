class CourseGrades:
    def __init__(self,course = '',section = '',semester='',year='',grades=[]):
        self.course = course
        self.section = section
        self.semester = semester
        self.year = year
        self.grades = grades
    def getGrades(self):
        return self.grades
    def printStudents(self):
        for i in self.grades:
            print(i)
    def averages(self):
        newlist = []
        Quize = 0
        Homework = 0
        labs = 0
        for i in self.grades:
            iavg=i.averageGrades()
            Quize += iavg[0]
            Homework += iavg[1]
            labs += iavg[2]
        if len(self.grades) != 0:
            avg_q= round(Quize/len(self.grades))
            avg_h = round(Homework/len(self.grades))
            avg_l = round(labs/len(self.grades))
            newlist = [avg_q,avg_h,avg_l]
        else:
            newlist = [0,0,0]
        return newlist
    def addStudent(self,student):
        self.grades.append(student)
    def __str__(self):
        res='course:'+self.course + '\nsection:' + self.section + '\nsemester:' +self.semester + '\nyear:' + str(self.year) + '\naverage:' +str(self.averages())
        return res
      
        
            
if __name__ == '__main__':
    course = str(input('course: '))
    section = str(input('section: '))
    semester = str(input('semester: '))
    year = int(input('year: '))
    print(CourseGrades(course,section,semester,year))