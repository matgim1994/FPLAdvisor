from django.views.generic import TemplateView
from .models import OverallStatistics
from .utils import get_plot
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64


class HomeView(TemplateView):
    template_name = "home.html"

class OverallStatisticsView(TemplateView):
    template_name = "overall.html"

def plot(request):
    qs = OverallStatistics.objects.all()
    x = [x.gameweek for x in qs]
    y = [y.average_score for y in qs]
    chart = get_plot(x, y)
    return render (request, 'plot.html', {'chart' : chart})
