class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_grades = 0
        total_courses = 0

        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_courses += len(grades)

        if total_courses == 0:
            return 0

        return total_grades / total_courses

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print(f'Review cannot be made, {student.name} is not enrolled in {course}.')

# Пример использования:
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades['Python'] = [8, 9, 10]

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_student(best_student, 'Python', 9)

print(f'Average grade for {cool_lecturer.name} {cool_lecturer.surname}: {cool_lecturer.get_average_grade()}')
print(f"Grades for {best_student.name} {best_student.surname}: {best_student.grades}")
