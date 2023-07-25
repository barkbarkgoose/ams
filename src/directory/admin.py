from django.contrib import admin
from directory.models import Member, Household


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000


@admin.register(Household)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000
