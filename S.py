class Student:
    def __init__(self):
        self.english_skills = 0
        self.code_skills = 0
        self.other_skills = 0

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

    def get_skills(self):
        print(self.english_skills)
        print(self.code_skills)
        print(self.other_skills)


if __name__ == '__main__':
    student = Student()
    student.study()
    student.get_skills()
