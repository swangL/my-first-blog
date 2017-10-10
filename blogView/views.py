from django.shortcuts import render
from django.views.generic import TemplateView

# View of the homepage
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# About view, when link clicked
class AboutPageView(TemplateView):
    template_name="about.html"
