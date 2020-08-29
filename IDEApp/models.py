from django.db import models

import subprocess
import os
import time
import sys
# Create your models here.


class TestCases(models.Model):
    id = models.AutoField(primary_key=True)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    inp = models.TextField()
    out = models.TextField()

    def __str__(self):
        return '%s %s' % (self.problem_id, self.id)


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    defination = models.TextField()

    def __str__(self):
        return '%s' % (self.title)


class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()


class IDE(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    code = models.TextField()
    inp = models.TextField(null=True)
    output = models.TextField(null=False, default="No ouput")

    def showOutput(self):
        path = self.makeFile(self.title, self.code)

        self.output = self.runCpp(path)

    def save(self, *args, **kwargs):
        self.showOutput()
        super().save(*args, **kwargs)

    def makeFile(self, name, code):
        name = name.replace(" ", "_")
        name = "G:\\SEM - 4\\Python\\Django_framework\\IDE\\IDE\\IDEApp\\Progs\\"+name+".cpp"
        with open(name, 'w') as f:
            code = code.replace("\r", "")
            f.write(code)
        return name

    def runCpp(self, path):
        runs = subprocess.run(
            ['g++', '-D', 'AUTO', '-O2', '-std=c++14', '-D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC', '-Wall', path, '-o', 'a.exe'], text=True, capture_output=True)
        if runs.returncode != 0:
            return "error!!!"
        else:
            data, temp = os.pipe()
            ins = self.inp
            ins = ins.strip()
            os.write(temp, bytes(str(ins).encode()))
            os.close(temp)
            start_time = time.process_time()
            s = subprocess.check_output(
                ['a.exe'], stdin=data, shell=True)
            output = s.decode("utf-8")
            output = output.replace("\r", "")
            return output

    def __str__(self):
        return str(self.title)
