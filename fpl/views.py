from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from fpl.models import OverallStatistics, Player
from fpl.utils import get_plot


class HomeView(TemplateView):
    template_name = "home.html"


class OverallStatisticsView(TemplateView):
    template_name = "overall.html"


class PlayersView(ListView):
    model = Player
    template_name = "players_list.html"


class PlayerDetailView(DetailView):
    model = Player
    template_name = "player_detail.html"


def plot(request):
    qs = OverallStatistics.objects.all()
    x = [x.gameweek for x in qs]
    y = [y.average_score for y in qs]
    chart = get_plot(x, y)
    return render(request, 'plot.html', {'chart': chart})
