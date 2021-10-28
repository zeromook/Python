class Score:

    def __init__(self, student):
        tmp = student.split(",")
        self.name = tmp[0]  #존
        self.midterm = int(tmp[1])  #90
        self.final = int(tmp[2])    #90
        self.assignment = int(tmp[3]) #0
        self.score = None
        self.grade = None

    def total_score(self):
        test_score = ((self.midterm + self.final) / 2) * 0.8  #72
        if self.assignment >= 3:
            assign_score = 20
        elif self.assignment >= 2:
            assign_score = 10
        elif self.assignment >= 1:
            assign_score = 5
        else:
            assign_score = 0
        self.score = test_score + assign_score

    def total_grade(self):
        if self.assignment == 0:
            grade = "F"
        elif self.score >= 90:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        else:
            grade = "F"

        self.grade = grade
        return grade


student_john = Score("john,90,90,0")
aa = student_john.total_score()
bb = student_john.total_grade()
print(aa, bb, student_john.score, student_john.grade)