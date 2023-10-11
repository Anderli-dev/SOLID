from abc import abstractmethod


class Human:
    def __init__(self):
        self.english_skills = 0
        self.code_skills = 0
        self.other_skills = 0

    @abstractmethod
    def study(self):
        pass

    def get_skills(self):
        print(self.english_skills)
        print(self.code_skills)
        print(self.other_skills)


class Student(Human):
    def study(self):
        self.learn_english()
        self.learn_code()
        self.learn_other()

    def learn_english(self):
        self.english_skills += 1
        # other code

    def learn_code(self):
        self.code_skills += 1
        # other code

    def learn_other(self):
        self.other_skills += 1
        # other code


class Scholar(Human):
    def study(self):
        self.learn_english()

    def learn_english(self):
        self.english_skills += 1
        # other code


if __name__ == '__main__':
    student = Student()
    student.study()
    student.get_skills()

    scholar = Scholar()
    scholar.study()
    scholar.study()
    scholar.get_skills()
