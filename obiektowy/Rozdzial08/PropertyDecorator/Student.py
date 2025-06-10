# Używanie właściwości w celu (pośredniego) uzyskania dostępu do danych w obiekcie.

class Student():

    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)('Nowa wartość: ' + str(newGrade) + ', jest nieprawidłowego typu.')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError('Nowa wartość: ' + str(newGrade) + ', musi być z przedziału od 0 do 100.')
        self.__grade = newGrade
