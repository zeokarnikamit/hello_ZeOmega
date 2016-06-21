# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from os.path import isfile, join, isdir
from os import listdir
import re


def im_dir(dir_path):
    for p_file in listdir(dir_path):
        if isfile(join(dir_path, p_file)):
            if p_file != '__init__.py':
                im_file(join(dir_path, p_file))
        elif isdir(join(dir_path, p_file)):
            im_dir(join(dir_path, p_file))


def im_file(file_path):
    file_names = open('check_files1.txt', 'a')
    filename = file_path.split('/')[-1]
    ext = filename.split('.')[-1]
    if ext == 'py':
        f_open = open(file_path)
        file_lines = f_open.readlines()
        f_open.close()
        li_no = 0
        for i, line in enumerate(file_lines):
            if re.search(r'\bDateTime\b', line) and '#' not in line:
                if li_no == 0:
                    file_names.write('------------{}----------'.format(file_path[36:]))
                    file_names.write('\n')
                file_names.write('{0}: {1}'.format(i, line))
                file_names.write('\n')
                li_no += 1
    file_names.close()


if __name__ == '__main__':
    im_dir('/home/local/PALYAM/kamit/workStation/jiva_buildout/src')
