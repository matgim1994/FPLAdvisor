from django.contrib import admin
from django.contrib.auth.models import User

from fpl.models import Player, Team, OverallStatistics, FPLManager, Event, Fixture


@admin.action(description="Predict for all fixtures in this event")
def predict_for_all_fixtures(modeladmin, request, queryset):
    for event in queryset:
        print(event)
        # TODO Save to database
        pass


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'second_name']


class EventAdmin(admin.ModelAdmin):
    actions = [predict_for_all_fixtures]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Player, PlayerAdmin)
admin.site.register(FPLManager)
admin.site.register(Event, EventAdmin)
admin.site.register(Fixture)
admin.site.register(OverallStatistics)
