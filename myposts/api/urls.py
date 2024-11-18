from django.urls import path
from .views import AuthorListView, PostListView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name="author_list"),
    path('posts/', PostListView.as_view(), name="post_list"),
]
