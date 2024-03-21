from django.contrib import admin
from fpl.models import Player, Club
from fpl.models import OverallStatistics


class PlayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Player, PlayerAdmin)

class ClubAdmin(admin.ModelAdmin):
    pass
admin.site.register(Club, ClubAdmin)

admin.site.register(OverallStatistics)