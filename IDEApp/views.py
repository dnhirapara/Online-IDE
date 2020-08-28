from django.shortcuts import render
from django.http import HttpResponse
from .IDEForm import Editor
from .models import IDE
from .serializers import IDESerializer
from rest_framework import viewsets

import subprocess
import os
import time
import sys
# Create your views here.


def index(request):
    return HttpResponse(runCpp('G:/SEM - 4/Python/Django_framework/IDE/IDE/IDEApp/Progs/a.cpp'))


class IDEViewSet(viewsets.ModelViewSet):
    queryset = IDE.objects.all().order_by('id')
    print("exe")
    serializer_class = IDESerializer


def codeit(request):
    form = Editor()
    text = ""
    if request.method == "POST":

        form = Editor(request.POST)
        print(request.POST['code'])
        path = makeFile(request.POST['title'].rstrip(), request.POST['code'])
        text = runCpp(path, (str(request.POST['inp'])).strip())
        # print(form)
        # if form.is_valid():
        #     post = form.save()
        #     form.save()
        #     print("ID"+str(post.id))
    else:
        form = Editor()
    # text = IDE.objects.all()
    text = text.strip()
    # print(repr(request.POST['inp']))
    print(text.split('\n'))
    return render(request, 'IDE/index.html', {'form': form, "text": {"lines": text.split('\n')}})


def makeFile(name, code):
    name = name.replace(" ", "_")
    name = "G:\\SEM - 4\\Python\\Django_framework\\IDE\\IDE\\IDEApp\\Progs\\"+name+".cpp"
    with open(name, 'w') as f:
        code = code.replace("\r", "")
        f.write(code)
    return name


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
