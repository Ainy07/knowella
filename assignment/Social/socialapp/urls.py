from django.urls import path
from .views import HotTopicsView, CategoryPostsView, SearchPostsView


urlpatterns = [

    path("hot-topics/", HotTopicsView.as_view()),

    path("posts/", CategoryPostsView.as_view()),

    path("search/", SearchPostsView.as_view()),

]