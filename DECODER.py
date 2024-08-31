#__________________| INFO |___________________#
#______SCRIPT ENCRYPTED BY PYTHON 3.0
#______CODING BY: MrDevilEx
#______GITHUB : https://github.com/MrDevilEx
#________________| SCRIPT DATA |_____________#
import os
import py_compile
import marshal
import struct
import importlib.util

def decode_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        magic = f.read(4)
        moddate = f.read(4)
        code = marshal.load(f)
    return code

if __name__ == '__main__':
    pyc_file = 'example.pyc'
    code = decode_pyc(pyc_file)
    exec(code)
