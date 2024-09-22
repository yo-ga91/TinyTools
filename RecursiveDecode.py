#! /usr/bin/python3.5
# -*- coding: utf-8 -*-


import os
import sys


def decode_file(file_name="test",file_type='utf-8'):
    content=''
    with open(file_name, 'r') as file:
        content=file.read()
    try:    
        with open(file_name, 'w', encoding=file_type) as file_out:
            file_out.write(content)
    except:
        return file_name

def get_file_list(target=os.getcwd()):
    r_file_list=[]
    for dirpath, _, filenames in os.walk(target):
        for filename in filenames:
            r_file_list.append(os.path.join(dirpath, filename))
    return r_file_list


def main_def (my_args):
    try:
        my_args.index('-h')
        print('''  fileencod.py -t "/home/user/" -en "utf-8"
  This script performs a recursive search for files in the specified directory and rewrites the found files to the specified encoding
    -h    help - print help  \n
    -t target dir (default=current directory)
    -en out file encoding (default=utf-8), examp ascii, cp1251, utf-8, utf-16
''')
    except ValueError:
        pass

    try:
        my_args.index('help')
        print('''  fileencod.py -t "/home/user/" -en "utf-8"
  This script performs a recursive search for files in the specified directory and rewrites the found files to the specified encoding
    -h    help - print help  \n
    -t target dir (default=current directory)
    -en out file encoding (default=utf-8), examp ascii, cp1251, utf-8, utf-16
''')
    except ValueError:
        pass

    if os.name == 'nt':
        my_args[my_args.index('-t')+1]=my_args[my_args.index('-t')+1].replace('\\','\\\\')

    print(f"Find files in dir \n {my_args[my_args.index('-t')+1]}")

    print('start')
    file_list=get_file_list()
    if os.name=='nt':
       for i in range(0,len(file_list)):
           file_list[i]=file_list[i].replace('\\','\\\\')

    for item in file_list:
        print(item)
    bad_decode=[]    
    for file in file_list:
        bad_decode.append(decode_file(file,my_args[my_args.index('-en')+1]))
        

    print('End')
    print('Problemfiles to decode \n')
    print(bad_decode, sep='\n')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main_def(sys.argv)
    else:
        print('''  fileencod.py -t "/home/user/" -en "utf-8"
  This script performs a recursive search for files in the specified directory and rewrites the found files to the specified encoding
    -h    help - print help  \n
    -t target dir (default=current directory)
    -en out file encoding (default=utf-8), examp ascii, cp1251, utf-8, utf-16
''')
        
