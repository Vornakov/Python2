# Задание No1
# 📌 Написать функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное
# имя, если оно передано. Далее счётчик файлов и расширение.

import os
from string import ascii_lowercase, digits
from random import choices, randint
from os import path
import shutil

__all__ = ['create_files', 'extensions', 'is_dir_exists',
           'create_list_file_names', 'rename_files_in_dir']

LEN_MIN = 6
LEN_MAX = 15
BYTE_MIN = 256
BYTE_MAX = 1024
FILE_QTS = 20
PATH_DIR = './ex_01'
FILE_END_NAME = 'XXX'
DIGIT_COUNT = 3


def rename_files_in_dir(init_ext: str, end_ext: str, region: list[int],
                        digit_qty: int = DIGIT_COUNT,
                        file_end: str = '') -> None:
    create_list_file_names()
    count = 1
    for name in create_list_file_names():
        if init_ext == name.split('.')[-1]:
            nums = '0' * (digit_qty - len(str(count))) + str(count)
            new_name = f'{name[region[0]:region[1]]}{file_end}_{nums}.{end_ext}'
            os.replace(name, new_name)
            count += 1


def create_files(extension: str, len_min: int=LEN_MIN, len_max: int=LEN_MAX, byte_min: int=BYTE_MIN,
                 byte_max: int=BYTE_MAX, quantity: int=FILE_QTS) -> None:
    for i in range(quantity):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(len_min, len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(byte_min, byte_max)))
        with open(rf'{name}.{extension}', 'wb') as f:
            f.write(data)


def extensions(**kwargs):
    for ext, qty in kwargs.items():
        create_files(extension=ext, quantity=qty)


def is_dir_exists(directory=PATH_DIR, **kwargs) -> None:
    if not path.exists(directory):
        os.mkdir(directory)
    os.chdir(directory)
    extensions(**kwargs)


def create_list_file_names():
    for dir_path, dir_name, file_name in os.walk(os.path.join(os.getcwd())):
        return file_name


if __name__ == '__main__':
    is_dir_exists(rf'{PATH_DIR}', gif=8, txt=12, jpeg=16)
    rename_files_in_dir('jpeg', 'md', [4, 8], 4, 'NAME')