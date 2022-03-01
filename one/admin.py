from django.contrib import admin
from .models import Student


class StudentDetailInline(admin.StackedInline):
    model = Student


# class StudentAdmin(admin.ModelAdmin):
#     inlines = [StudentDetailInline]


admin.site.register(Student)
