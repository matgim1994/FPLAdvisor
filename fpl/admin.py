from django.contrib import admin
from fpl.models import Player, Club


class PlayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Player, PlayerAdmin)

class ClubAdmin(admin.ModelAdmin):
    pass
admin.site.register(Club, ClubAdmin)