from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

class OverallStatus(TemplateView):
    template_name = "overall.html"