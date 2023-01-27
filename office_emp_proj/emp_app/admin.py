from django.contrib import admin
from .models import Role,Department,Employee


class Deptlist(admin.ModelAdmin):
    list_display = ("name","location")

class Rolelist(admin.ModelAdmin):
    pass

class Emplist(admin.ModelAdmin):
    list_display = ('first_name','last_name','dept','role','salary','bonus','phone','hire_date')


admin.site.register(Employee,Emplist)
admin.site.register(Role)
admin.site.register(Department,Deptlist)

# Register your models here.
