from django.contrib import admin
from django.contrib.auth.models import User

from fpl.models import Player, Team, OverallStatistics, FPLManager


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'second_name']


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Player, PlayerAdmin)
admin.site.register(FPLManager)
admin.site.register(OverallStatistics)
