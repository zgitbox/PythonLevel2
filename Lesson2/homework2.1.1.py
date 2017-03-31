# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:22:15 2017

@author: Zinfir

1. Разработать модель предметной области в соответствии с вариантом:
1.1 Предметная область - предприятие. Разработать класс Enterprise, описывающий
работу с предприятием. Разработать класс People, описывающий человека, человек
характеризуется параметрами: фамилия, имя, отчество, дата рождения, телефон.
Разработать класс Employees на базе класса People, сотрудник характеризуется
следующими параметрами: уникальный идентификатор сотрудника, код отдела,
заработная плата.
"""
# Класс "Предприятие" 
# Т.к. в задании ничего про предприятие не написано, то делаю вольный минимум, без сеттеров/геттеров
#------------------------------------------------------------------------------
class Enterprise:
    
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def __str__(self):
        return 'Enterprise <Company name: {0}; Employee count: {1}>'.format(self.name, self.employee_count())
    
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def rem_employee(self, employee):
        self.employees.remove(employee)
        
    def employee_count(self):
        return len(self.employees)
#------------------------------------------------------------------------------
# Класс "Человек" 
#------------------------------------------------------------------------------
class Person:
    
    def __init__(self, last_name, first_name, mid_name, birth_dt, phone_num):
        self.last_name  = last_name
        self.first_name = first_name
        self.mid_name   = mid_name
        self.birth_dt   = birth_dt
        self.phone_num  = phone_num
    
    def __str__(self):
        return 'Person <{0} {1} {2}>'.format(self.last_name, self.first_name, self.mid_name)
#------------------------------------------------------------------------------
# Класс "Сотрудник" 
#------------------------------------------------------------------------------
class Employee(Person):
    
    def __init__(self, last_name, first_name, mid_name, birth_dt, phone_num, emp_id, depart_id, salary):
        super().__init__(last_name, first_name, mid_name, birth_dt, phone_num)
        self.emp_id     = emp_id
        self.depart_id  = depart_id
        self.salary     = salary
        
    def __str__(self):
        return 'Employee <{0}: {1} {2} {3}>'.format(self.emp_id, self.last_name, self.first_name, self.mid_name)
#------------------------------------------------------------------------------        
# Тест
#------------------------------------------------------------------------------
enterprise = Enterprise('Alphabet')
print(enterprise)

employee1 = Employee('Brin', 'Sergey', 'Michaylovich', '21.03.1973', '+18880000001', '00000001', 'top', '1')
print(employee1)
enterprise.add_employee(employee1)
print(enterprise)

enterprise.add_employee(Employee('Black', 'John', '', '09.09.1989', '+18567834001', '03423401', 'any', '10500'))
print(enterprise)

enterprise.rem_employee(employee1)
print(enterprise)