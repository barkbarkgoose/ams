from django.contrib import admin
from ministering.models import Assignment, BrotherComp, SisterComp


@admin.register(Assignment)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000


@admin.register(BrotherComp)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000


@admin.register(SisterComp)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000
