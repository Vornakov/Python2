# Задание No7
# 📌 Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# 📌 Каждая группа включает файлы с несколькими расширениями.
# 📌 В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from string import ascii_lowercase, digits
from random import choices, randint
from os import path
import shutil

__all__ = ['make_files', 'many_extensions', 'check_dir', 'make_dirs',
           'list_file_names', 'sort_files_by_dirs']

LEN_MIN = 6
LEN_MAX = 30
BYTE_MIN = 256
BYTE_MAX = 4096
FILE_QTS = 42
PATH_DIR = './ex_07_from_sem07'

file_types = {'video': ('mp4', 'mov', 'avi', 'wmv'),
              'image': ('jpeg', 'png', 'gif', 'tiff'),
              'text': ('txt', 'doc', 'md', 'rtf', 'pdf'), }


def make_files(extension: str, len_min: int=LEN_MIN, len_max: int=LEN_MAX, byte_min: int=BYTE_MIN,
               byte_max: int=BYTE_MAX, quantity: int=FILE_QTS) -> None:

    for i in range(quantity):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(len_min, len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(byte_min, byte_max)))
        with open(rf'{name}.{extension}', 'wb') as f:
            f.write(data)


def many_extensions(**kwargs):
    for ext, qty in kwargs.items():
        make_files(extension=ext, quantity=qty)


def check_dir(directory=PATH_DIR, **kwargs) -> None:
    if not path.exists(directory):
        os.mkdir(directory)
    os.chdir(directory)
    many_extensions(**kwargs)


def make_dirs(**kwargs):
    os.chdir('..')
    for key in kwargs.keys():
        if not path.exists(key):
            os.mkdir(key)


def list_file_names(directory=PATH_DIR):
    for dir_path, dir_name, file_name in os.walk(os.path.join(os.getcwd(), directory)):
        return file_name


def sort_files_by_dirs(directory=PATH_DIR, **kwargs)  -> None:
    make_dirs(**file_types)
    list_file_names()
    for name in list_file_names():
        for key, value in kwargs.items():
            if name.split('.')[-1] in value:
                shutil.move(os.path.join(directory, name),
                            os.path.join(os.getcwd(), key))


if __name__ == '__main__':
    check_dir(rf'{PATH_DIR}', gif=4, doc=3, txt=5, jpeg=8,
              mp4=2, mp3=1, avi=6, zip=7, bmp=4)
    sort_files_by_dirs(**file_types)