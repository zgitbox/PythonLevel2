# -*- coding: utf-8 -*-
'''
Homework Lesson1

1. Записать строку символов в текстовый файл и вывести содержимое файла.
2. Записать строку символов в файл, явным указанием кодировки utf-8, вывести содержимое файла.
3. Декодировать содержимое файла из предыдущего задания.
4. Записать строку символов в двоичный файл и вывести содержимое файла.
5. Записать строку символов в файл, явным указанием кодировки latin-1, вывести содержимое файла.
6. Декодировать содержимое файла из предыдущего задания.
7. * Определить из jpg файлов был создан ранее всех.
'''
print('-----1-----')
open('cat.txt', 'w').write('Записываю строку символов в текстовый файл и вывожу содержимое файла.')
print(open('cat.txt', 'r').read())

print('\n-----2-----')
open('cat.txt', 'w', encoding='utf-8').write('Записываю строку символов в файл, c явным указанием кодировки utf-8, и вывожу содержимое файла.')
print(open('cat.txt', 'r').read())

print('\n-----3-----')
cat = open('cat.txt', 'rb').read()
print(cat.decode())
# Если открывать в режиме r, то выводится ошибка AttributeError: 'str' object has no attribute 'decode'
# так и задумано или нужно ещё что-то сделать чтобы он открылся в режиме r?

print('\n-----4-----')
open('cat', 'wb').write(b'I write a line of symbols into binary file and print his content.')
print(open('cat', 'rb').read())

print('\n-----5-----')
open('cat', 'w', encoding='latin-1').write('I write a line of symbols into binary file with latin-1 coding and print his content.')
print(open('cat', 'r').read())

print('\n-----6-----')
cat = open('cat', 'rb').read()
print(cat.decode())