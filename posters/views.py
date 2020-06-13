from datetime import timezone
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView)
from . import models

# Create your views here.


class HomePageView(TemplateView):
    template_name = "posters/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = "Home"
        return context


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = "posters/post_delete.html"
    slug_field = 'id'
    slug_url_kwarg = 'id'
    success_url = reverse_lazy('posters:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = "Delete Post"
        return context


class PostCreateView(LoginRequiredMixin,CreateView):
    model = models.Post
    template_name = "posters/post_create.html"
    fields = ('title', 'body')
    login_url = '/userLogin/login/'
    redirect_field_name = 'posters/post_detail.html'
    def is_publishing(self):
        return 'Publishing' in self.request.POST

    def is_drafting(self):
        return 'Saving' in self.request.POST

    def form_valid(self, form):
        user_author = User.objects.get(pk=self.user_creating_post_id)
        new_post = form.save(commit=False)
        new_post.is_draft = self.is_drafting()
        new_post.is_publicated = self.is_publishing()
        new_post.author = user_author
        new_post.save()
        return HttpResponseRedirect(reverse('posters:detail', kwargs={'id': new_post.id}))

    def post(self, request, *args, **kwargs):
        self.user_creating_post_id = request.user.id
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = "New Post"
        return context


class PostUpdateView(UpdateView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ('title', 'body')
    context_object_name = 'post'
    model = models.Post
    template_name = 'posters/post_update_form.html'

    def is_publishing(self):
        return 'Publishing' in self.request.POST

    def is_drafting(self):
        return 'Saving' in self.request.POST

    def form_valid(self,form):
        post = form.save(commit=False)
        if not post.is_publicated:
            post.is_draft = self.is_drafting()
            post.is_publicated = self.is_publishing()
        post.save()
        return HttpResponseRedirect(reverse('posters:detail',kwargs={'id':post.id}))

class PostDetailView(DetailView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'post'
    model = models.Post

    def post(self, request, *args, **kwargs):
        comment_to_delete = models.Comment.objects.filter(pk=request.POST.get("comment_id"))
        comment_to_delete.delete()

        return HttpResponseRedirect(reverse('posters:detail', kwargs=kwargs))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = context["post"].title
        return context


class PostListView(ListView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    model = models.Post
    context_object_name = 'posts'

    def get_queryset(self):
        return models.Post.objects.filter(is_publicated=True).order_by('-published_date')

class DraftPostListView(LoginRequiredMixin,ListView):
    slug_field = 'id'
    slug_url_kwarg = 'id'
    model = models.Post
    template_name = 'posters/draft_list.html'
    context_object_name = 'posts'
    login_url = '/userLogin/login'
    redirect_field_name = ''
    def get_queryset(self):
        return models.Post.objects.filter(is_draft = True,author = self.request.user.id)
    

class CommentDeleteView(DeleteView):
    model = models.Comment
    slug_field = 'id'
    slug_url_kwarg = 'comment_id'
    context_object_name = 'comment'
    template_name= 'posters/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('posters:detail',kwargs={'id':self.object.post.id})

class CommentCreateView(CreateView):
    model = models.Comment
    fields = ('author', 'body_text')
    template_name = "posters/comment_create.html"

    def get_related_post(self, primaryKey):
        self.related_post = models.Post.objects.get(pk=primaryKey)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.post = self.related_post
        new_comment.save()
        return HttpResponseRedirect(reverse('posters:detail', kwargs={"id": self.related_post.id}))

    def post(self, request, *args, **kwargs):
        self.get_related_post(kwargs["id"])
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actual_page"] = "Comment"
        return context
