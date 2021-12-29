from datetime import date
from app import salary
from app.db import people

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(str(date.today()))
    print("End")
