from abc import abstractmethod


class Human:
    def __init__(self, english_skills, code_skills, other_skills):
        self.english_skills = english_skills
        self.code_skills = code_skills
        self.other_skills = other_skills
        self.money = 0

    @abstractmethod
    def study(self):
        pass

    def get_skills(self):
        print(self.english_skills)
        print(self.code_skills)
        print(self.other_skills)

class WorkingHuman(Human):
    def work(self, salary):
        self.money += salary

    def get_money(self):
        print(self.money)


class Student(WorkingHuman):
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

    def __init__(self, english_skills, code_skills, other_skills, read_skills):
        super().__init__(english_skills, code_skills, other_skills)
        self.read_skills = read_skills

    def study(self):
        self.learn_english()

    def learn_english(self):
        self.english_skills += 1
        # other code

    def get_skills(self):
        super().get_skills()
        print(self.read_skills)


class Teacher(WorkingHuman):
    pass


if __name__ == '__main__':
    student = Student(0, 0, 0)
    student.study()
    student.work(100)
    student.get_skills()
    student.get_money()

    print("--------")
    scholar = Scholar(0, 0, 0, 5)
    scholar.study()
    scholar.study()
    scholar.get_skills()

    print("--------")
    teacher = Teacher(5,  5, 5)
    teacher.work(1000)
    teacher.get_skills()
    teacher.get_money()
