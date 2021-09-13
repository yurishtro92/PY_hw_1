from datetime import date
from application import salary
from db import people
if __name__ == '__main__':
    print('Current date:', str(date.today()))
    salary.calculate_salary()
    people.get_employees()


