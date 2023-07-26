from django.contrib import admin
from ministering.models import BrotherComp, SisterComp


@admin.register(BrotherComp)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000


@admin.register(SisterComp)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000
