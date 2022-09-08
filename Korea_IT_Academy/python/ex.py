class Student:
    def __init__(self, ID = None, Name = None, Score = None):
        self.studentID = ID
        self.studentName = Name
        self.studentScore = Score

    def setID(self, ID):
        self.studentID = ID
        print('학번이 {}(으)로 바뀌었습니다.'.format(self.studentID))

    def getID(self):
        return self.studentID

    def setName(self, Name):
        self.studentName = Name
        print('이름이 {}(으)로 바뀌었습니다.'.format(self.studentName))

    def getName(self):
        return self.studentName

    def setScore(self, Score):
        self.studentScore = Score
        print('성적이 {}(으)로 바뀌었습니다.'.format(self.studentScore))

    def getScore(self):
        return self.studentScore

    def checkScore(self):
        if self.studentScore == 'F':
            print('{}은 낙제입니다.'.format(self.studentScore))
        elif self.studentScore == 'A':
            print('{}은 우등생입니다.'.format(self.studentScore))
        else:
            print('{}은 학교를 잘 다니고 있습니다.'.format(self.studentScore))

s1 = Student()
s1.setID(971001)
s1.setName('유세종')
s1.setScore('A')

print(s1.getID())
s1.checkScore()
