# 2. Академія розробки програмного забезпечення викладає два типи курсів: місцеві
# курси, які проводяться в деяких місцевих лабораторіях академії та виїзні курси, що
# проводяться в іншому місті за межами штаб-квартири академії.
#
# Кожен курс має назву,
# викладача, що призначений для його викладання та програму курсу (список тем).
#
# Кожен викладач має ім’я та знає курси, які він викладає. Інформація про всі типи курсів і про
# викладачів має бути надрукована у тексті, зручному для читання людиною.
#
# Усі ваші курси повинні доповнювати загальний курс ICourse. Викладачі повинні
# впроваджувати ITeacher.
#
# Місцеві та виїзні курси повинні впроваджувати ILocalCourse та
# IOffsiteCourse відповідно.
#
# Курси та викладачі повинні створюватися лише через
# інтерфейс ICourseFactory, реалізований класом під назвою CourseFactory.
#
# Напишіть програму, яка формуватиме курси академії розробки програмного
# забезпечення.

from abc import *


class ICourseFactory(ABC):

    @abstractmethod
    def __init__(self):
        pass


class ICourse(ICourseFactory):

    def __init__(self, course_name, teacher, course_program, type_course):
        self.course_name = course_name
        self.teacher = teacher
        self.course_program = course_program
        self.type_course = type_course


class ILocalCourse(ICourse):

    def __init__(self, course_name, teacher, course_program, type_course="Local Course"):
        super().__init__(course_name, teacher, course_program, type_course)


class IOffsiteCourse(ICourse):

    def __init__(self, course_name, teacher, course_program, type_course="Offsite Course"):
        super().__init__(course_name, teacher, course_program, type_course)


class ITeacher(ICourseFactory):

    def __init__(self, teacher, list_course: list):
        self.teacher = teacher
        self.list_course = list_course


class CourseFactory:

    def __init__(self, choice_action):

        def question_choice(meseg, action: (tuple, list)):
            print(meseg)
            for i in range(len(action)):
                print(i+1, " -> ", action[i])
            n = int(input())
            return action[n-1]

        if choice_action == "course":

            type_course = question_choice("Який тип курсу потрібно створити?", ('Local Course', 'Offsite Course'))

            course_name = str(input("Введіть назву курсу"))
            teacher = str(input("Введіть викладача курсу"))
            course_program = str(input("Введіть програму курсу")).split(", ")
            if type_course == "Local Course":
                ILocalCourse(course_name, teacher, course_program, type_course)

            else:
                IOffsiteCourse(course_name, teacher, course_program, type_course)

        else:
            teacher = str(input("Введіть викладача"))
            print("Введіть список предметів даного викладача (розділені через кому)")
            subgects = str(input()).split(", ")
            ITeacher(teacher, subgects)


