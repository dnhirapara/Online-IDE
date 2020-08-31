from django.contrib import admin
from .models import IDE, Problem, Submission, TestCases

# Register your models here.

admin.site.register(IDE)
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(TestCases)
