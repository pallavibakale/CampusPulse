from django.contrib import admin
from .models import Student, Ethnicity, Gender, Major, YearInSchool

admin.site.register(Student)
admin.site.register(Ethnicity)
admin.site.register(Gender)
admin.site.register(Major)
admin.site.register(YearInSchool)