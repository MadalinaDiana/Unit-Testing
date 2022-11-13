import math


class Rectangle:

    def __init__(self, lenght, width, color):
        self.lenght = lenght
        self.width = width
        self.color = color

    def describe(self):
        print(f'The rectangle has {self.lenght} lenght, {self.width}  width and color {self.color}. \n '
              f'has the perimeter {self.perimeter()}, aria {self.aria()}')

    def aria(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2 * self.aria()

    def change_color(self, new_color):
        self.color = new_color


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def aria(self):
        return math.pi * self.radius ** 2

    def describe(self):
        print(
            f'The arie of the circle is: {self.aria()}, color of the circle is {self.color} and have the diameter '
            f'{self.diameter()} and the circumference {self.circumference()}')

    def diameter(self):
        return self.radius * 2

    def circumference(self):
        return math.pi * self.diameter()


class Cont:
    def __init__(self, iban, holder_cont, balance):
        self.iban = iban
        self.holder_cont = holder_cont
        self.balance = balance

    def display_sold(self):
        print(f'The Holder {self.holder_cont} of the account {self.iban} has the balance {self.balance}')

    def debit_cont(self, amount):
        self.balance += amount
        return self.balance

    def credit_cont(self, amount):
        self.balance -= amount
        return self.balance

class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def describe(self):
        print(f'Name of the employee is {self.complet_name()} and has the salary on month {self.salary_month()}.')

    def complet_name(self):
        return self.name + ' ' + self.surname

    def salary_month(self):
        return self.salary

    def salary_annual(self):
        return self.salary * 12

    def salary_marriage(self, procent: int) -> float:
        self.salary += ((self.salary * procent) // 100)
        return self.salary
