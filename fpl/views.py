from django.shortcuts import render
from django.views.generic import TemplateView

from fpl.models import OverallStatistics
from fpl.utils import get_plot


class HomeView(TemplateView):
    template_name = "home.html"


class OverallStatisticsView(TemplateView):
    template_name = "overall.html"


def plot(request):
    qs = OverallStatistics.objects.all()
    x = [x.gameweek for x in qs]
    y = [y.average_score for y in qs]
    chart = get_plot(x, y)
    return render(request, 'plot.html', {'chart': chart})
