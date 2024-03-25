from django.contrib import admin
from django.contrib.auth.models import User

from fpl.models import Player, Team, FPLManager
from fpl.models import OverallStatistics
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class EmployeeInline(admin.StackedInline):
    model = FPLManager
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(OverallStatistics)
