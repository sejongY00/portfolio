class Student:
    __countOfStudent = 0
    __departure = '경영학과'

    def __init__(self, ID = 0, Name = '', Score = None):
        self.__studentID = ID
        self.__studentName = Name
        self.__studentScore = Score
        Student.__countOfStudent += 1

    def setID(self, ID):
        self.__studentID = ID
        print('학번이 {}(으)로 바뀌었습니다.'.format(self.__studentID))

    def getID(self):
        return self.__studentID

    def setName(self, Name):
        self.__studentName = Name
        print('이름이 {}(으)로 바뀌었습니다.'.format(self.__studentName))

    def getName(self):
        return self.__studentName

    def setScore(self, Score):
        self.__studentScore = Score
        print('성적이 {}(으)로 바뀌었습니다.'.format(self.__studentScore))

    def getScore(self):
        return self.__studentScore

    def getCountOfStudent():
        return Student.__countOfStudent

    def getDeparture():
        return Student.__departure



        def getData(self):
                return [self.__first, self.__second]
s1 = Student()
s2 = Student()
s1.setID(100)
s1.setName('James')
s1.setScore('F')

print(s1.getName())

print(Student.getCountOfStudent())