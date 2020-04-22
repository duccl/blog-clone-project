from django.urls import path,include
from . import views
app_name = 'posters'

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path("newPost/", views.PostCreateView.as_view(), name="new_post"),
    path("detail/<int:id>", views.PostDetailView.as_view(), name="detail"),
]
