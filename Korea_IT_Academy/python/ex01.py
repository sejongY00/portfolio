class FourCal:
    def __init__(self, first, second):
        self.__first = first
        self.__second = second

    def setData(self, first, second):
        self.__first = first
        self.__second = second

    def setFirst(self, first):
        self.__first = first

    def setSecond(self, second):
        self.__second = second

    def add(self):
        result = self.__first + self.__second
        return result

a = FourCal(1,2)
print(a.add())

a.setData(1,3)
print(a.add())

a.setFirst(2)
print(a.add())

a.setSecond(4)
print(a.add())