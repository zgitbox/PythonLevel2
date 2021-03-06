# -*- coding: utf-8 -*-
'''
Homework Lesson1

1. Записать строку символов в текстовый файл и вывести содержимое файла.
2. Записать строку символов в файл, явным указанием кодировки utf-8, вывести содержимое файла.
3. Декодировать содержимое файла из предыдущего задания.
4. Записать строку символов в двоичный файл и вывести содержимое файла.
5. Записать строку символов в файл, явным указанием кодировки latin-1, вывести содержимое файла.
6. Декодировать содержимое файла из предыдущего задания.
7. * Определить какой из jpg файлов был создан ранее всех.
'''
print('-----1-----')
open('1.txt', 'w').write('Записываю строку символов в текстовый файл и вывожу содержимое файла.')
print(open('1.txt', 'r').read())

print('\n-----2-----')
open('2.txt', 'w', encoding='utf-8').write('Записываю строку символов в файл, c явным указанием кодировки utf-8, и вывожу содержимое файла.')
print(open('2.txt', 'r').read())

print('\n-----3-----')
cat = open('2.txt', 'rb').read()
print(cat.decode())

# Есть очущение, что вторую половину заданий я понял неверно.
print('\n-----4-----')
open('4', 'wb').write(b'I write a line of symbols into binary file and print his content.')
print(open('4', 'rb').read())

print('\n-----5-----')
open('5', 'w', encoding='latin-1').write('I write a line of symbols into binary file with latin-1 coding and print his content.')
print(open('5', 'r').read())

print('\n-----6-----')
cat = open('cat', 'rb').read()
print(cat.decode())
