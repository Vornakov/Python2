"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

number = int(input())
number_1 = number
h = hex(number_1)
hex_strings = "0123456789abcdef"
hex_number = ""
REMAINS_HEX = 16

while number > 0:
    remains = number % REMAINS_HEX
    hex_string = hex_strings[remains]
    hex_number = hex_string + hex_number
    number //= REMAINS_HEX

if hex_number == h[2:]:
    print(f'{True}\t{hex_number = }\t{h[2:] = }')
else:
    print(f'{False}\t{hex_number = }\t{h[2:] = }')