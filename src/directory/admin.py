from django.contrib import admin
from directory import models as dmods

# Register your models here.
admin.site.register(dmods.Household)
admin.site.register(dmods.Member)
