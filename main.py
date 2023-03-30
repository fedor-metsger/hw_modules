
from datetime import date
from art import *
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    """
    Задача:
    1. Разработать структуру программы «Бухгалтерия»:
        main.py;
        application/salary.py;
        application/db/people.py.

    Main.py — основной модуль для запуска программы.
    В модуле salary.py функция calculate_salary.
    В модуле people.py функция get_employees.

    2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.

    3. Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.

    4. Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией.
        При желании можно написать программу с этим пакетом.
        Я выбрал пакет "art". В нём есть функция "tprint"
    :return:
    """
    print("Today's date is", date.today().strftime("%d/%m/%Y"))
    calculate_salary()
    get_employees()
    tprint("python", font="random")

if __name__ == '__main__':
    main()