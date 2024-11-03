print("Hi!")


class StudySubject:
    def __init__(self):
        self.name = input("Геометрія")
        self.hours = int(input(4))
        self.enable = bool(int(input(1)))

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')

class Student:
    def __init__(self):
        self.name = input("Олег")
        self.surname = input("Дон")
        self.studies = [2]
        num_subjects = int(input(2))
        for _ in range(num_subjects):
            subject = StudySubject()
            self.studies.append(subject)

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        for study in self.studies:
            study.info_study()

class Group:
    def __init__(self):
        self.group_name = input("С2118")
        self.age_category = input("Діти")
        self.students = [5]
        num_students = int(input(24))
        for _ in range(num_students):
            student = Student()
            self.students.append(student)

    def info_group(self):
        print(f'Group: {self.group_name} | Age Category: {self.age_category} | Number of Students: {len(self.students)}')
        for student in self.students:
            student.info_all()

group = Group()
group.info_group()
