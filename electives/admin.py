from django.contrib import admin

from .models import Electives,ElectiveSemester,ElectiveFaculty

# Register your models here.
admin.site.register(Electives)
admin.site.register(ElectiveSemester)
admin.site.register(ElectiveFaculty)