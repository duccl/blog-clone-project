from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from . import models
# Create your views here.
class HomePageView(TemplateView):
    template_name = "posters/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = "Home"
        return context


class PostCreateView(CreateView):
    model = models.Post
    template_name = "posters/post_create.html"
    fields = ('title','author','body')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = "New Post"
        return context
    


class PostDetailView(DetailView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'post'
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = context["post"].title
        print(context["post"].comments.all().count)
        return context
    
    
class PostListView(ListView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    model = models.Post
    context_object_name = 'posts'
