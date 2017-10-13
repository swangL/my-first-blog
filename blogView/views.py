from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Post
from django.utils import timezone

# View of the homepage
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'blogView/index.html', context=None)

# About view, when link clicked
class AboutPageView(TemplateView):
    template_name="blogView/about.html"

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'blogView/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogView/post_detail.html', {'post': post})
