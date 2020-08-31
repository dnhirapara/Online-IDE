from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .IDEForm import Editor
from .models import IDE, Submission, Problem, TestCases
from .serializers import IDESerializer
from rest_framework import viewsets

import json
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


def codeSubmit(request):
    text = ""
    response_data = {}
    response_data['msg'] = "error"
    print("code Run")
    if request.method == "POST":
        print(request.POST['code'])

        path = makeFile(request.POST['title'].rstrip(), request.POST['code'])
        inputs = ""
        problems = Problem.objects.all()[0]
        response_data['msg'] = "success"
        print(response_data)
        print(TestCases.objects.filter(problem_id=problems))
        k = 0
        answer = ""
        flag = False
        debug_msg = ""
        # for i in problems.testcases_set.all():
        for i in TestCases.objects.filter(problem_id=problems):
            text = runCpp(path, i.inp)
            k += 1
            answer += "#input :" + str(k)+"\n"+i.inp
            answer += "\nOutput:\n" + text
            answer += "\nAnswer:\n" + i.out + "\n\n"
            if (str(i.out).strip() != text.strip()):
                flag = True
                debug_msg = "Wrong Answer\n"
                debug_msg += "#input :" + str(k)+"\n"+i.inp
                debug_msg += "\nOutput:\n" + text
                debug_msg += "\nAnswer:\n" + i.out + "\n\n"
                debug_msg.replace("\n", "<br/>")
            break
            print(i.inp)
            print(i.out)
            print(text)
        # return JsonResponse(response_data)
        if (flag):
            response_data['out'] = debug_msg
        else:
            response_data['out'] = "Accepted"
        form = Submission(problem_id=problems,
                          code=request.POST['code'], result=answer)
        form.save()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def codeRun(request):
    text = ""
    response_data = {}
    response_data['msg'] = "error"
    print("code Run")
    if request.method == "POST":
        path = makeFile(request.POST['title'].rstrip(), request.POST['code'])
        inputs = ""
        print(request.POST.get('chk_input'))
        if request.POST.get('chk_input') == '1':
            inputs = (str(request.POST['inp'])).strip()
            print(inputs)
        text = runCpp(path, inputs)
        text = text.strip()
        response_data['out'] = text
        response_data['msg'] = "success"
        print(response_data)
        # return JsonResponse(response_data)
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    # text = ""
    # response_data = {}
    # response_data['msg'] = "error"
    # print("code Run")
    # if request.method == "POST":
    #     path = makeFile(request.POST['title'].rstrip(), request.POST['code'])
    #     inputs = ""
    #     print(request.POST.getlist('chk_input'))
    #     if request.POST.get('chk_input') == '1':
    #         inputs = (str(request.POST['input'])).strip()
    #     text = runCpp(path, inputs)
    #     text = text.strip()
    #     response_data['out'] = text
    #     response_data['msg'] = "success"
    #     print(response_data)
    #     return JsonResponse(response_data)
    # return JsonResponse(response_data)


def codeit(request):
    text = "123\n456"
    form = {"hello": "to"}
    return render(request, 'IDE/index.html')

# def codeit(request):
#     # form = Editor()
#     text = ""
#     if request.method == "POST":
#         # form = Editor(request.POST)
#         # print(request.POST['code'])
#         path = makeFile(request.POST['title'].rstrip(), request.POST['code'])
#         text = runCpp(path, (str(request.POST['inp'])).strip())
#         # print(form)
#         # if form.is_valid():
#         #     post = form.save()
#         #     form.save()
#         #     print("ID"+str(post.id))
#     # else:
#         # form = Editor()
#         # text = IDE.objects.all()
#     text = text.strip()
#     # print(repr(request.POST['inp']))
#     print(text.split('\n'))
#     form = {"hello": "to"}
#     return render(request, 'IDE/index.html', {'form': form, "text": {"lines": text.split('\n')}})


def makeFile(name, code):
    name = name.replace(" ", "_")
    name = "G:\\SEM - 4\\Python\\Django_framework\\IDE\\IDE\\IDEApp\\Progs\\"+name+".cpp"
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
