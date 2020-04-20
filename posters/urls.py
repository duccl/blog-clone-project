from django.urls import path
from . import views
app_name = 'posters'

urlpatterns = [
    path("",views.HomePageView.as_view(),name='home'),
    path("list/", views.PostListView.as_view(), name="list"),
    path("detail/<int:id>", views.PostDetailView.as_view(), name="detail"),
]
