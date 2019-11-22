import Second

base = {"teachers": {"Викладач ": ["курс-1", "курс-2", 'курс-3']},
        "course": {"Назва курсу": ("Імя викладача", ["програма курсу"], "Тип курсу")}}


def main():
    print()

    def check(rang, mes):
        while True:
            try:
                x = int(input())
                if x not in range(rang):
                    raise ValueError
                break
            except ValueError:
                print(mes)
        return x

    def question_choice(meseg, action: (tuple, list)):
        print(meseg)
        for i in range(len(action)):
            print(i, " -> ", action[i])
        n = check(len(action), "Виберіть вірний пункт")
        return action[n]

    action = question_choice("Що ви бажаєте добавити? ", ("course", "teacher"))
    new_action = Second.CourseFactory(action).info()

    if action == "course":

        base["course"][new_action[0]] = new_action[1::]


    else:
        base["teachers"][new_action[0]] = new_action[1]
    print(base)
main()