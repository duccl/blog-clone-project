from django.urls import path,include
from . import views
app_name = 'posters'

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path("newPost/", views.PostCreateView.as_view(), name="new_post"),
    path("detail/<int:id>", views.PostDetailView.as_view(), name="detail"),
    path("delete/<int:id>", views.PostDeleteView.as_view(), name="delete"),
    path("detail/<int:id>/new_comment", views.CommentCreateView.as_view(), name="new_comment"),
]
