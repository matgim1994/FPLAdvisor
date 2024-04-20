from django.contrib import admin
from django.contrib.auth.models import User

from fpl.models import Player, Team, OverallStatistics, FPLManager, Event, Fixture, PointsInFixture


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'second_name']


class EventAdmin(admin.ModelAdmin):
    actions = ['predict_for_all_fixtures']

    def predict_for_all_fixtures(self, request, queryset):
        for event in queryset:
            for fixture in event.fixture_set.all():
                for player in fixture.team_h.player_set.all() | fixture.team_a.player_set.all():
                    # TODO: Dodaj prediction, jak na razie mamy hardcodowane 1.0.
                    PointsInFixture.objects.update_or_create(player=player, fixture=fixture,
                                                             defaults={'predicted_points': 1.0,
                                                                       'actual_points': 0.0})

    
    predict_for_all_fixtures.short_description = "Predict for all fixtures in this event"


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Player, PlayerAdmin)
admin.site.register(FPLManager)
admin.site.register(Event, EventAdmin)
admin.site.register(Fixture)
admin.site.register(OverallStatistics)
