import subprocess
import os
import time
import sys

from django.conf import settings


def makeFile(name, code, extension):
    name = name.replace(" ", "_")
    name = settings.SUBMISSION_ROOT+name+"."+extension
    with open(name, 'w') as f:
        code = code.replace("\r", "")
        f.write(code)
    return name


def compileCpp(path):
    runs = subprocess.run(
        ['g++', '-D', 'AUTO', '-O2', '-std=c++14', '-D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC', '-Wall', path, '-o', 'a.exe'], text=True, capture_output=True)
    return not runs.returncode


def runCpp(path, inp):
    runs = subprocess.run(
        ['g++', '-D', 'AUTO', '-O2', '-std=c++14', '-D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC', '-Wall', path, '-o', 'a.exe'], text=True, capture_output=True)
    if runs.returncode != 0:
        return "error!!!"
    else:
        data, temp = os.pipe()
        ins = inp
        os.write(temp, bytes(str(ins).encode()))
        os.close(temp)
        start_time = time.process_time()
        s = subprocess.check_output(
            ['a.exe'], stdin=data, shell=True)
        output = s.decode("utf-8")
        output = output.replace("\r", "")
        return output
