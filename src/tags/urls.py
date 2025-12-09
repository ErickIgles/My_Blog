from django.urls import path

from . import views

app_name = 'tags'

urlpatterns = [
    path(
        '',
        views.TagListView.as_view(),
        name='tags'
    ),
    path(
        '<slug:slug>/',
        views.TagPostListView.as_view(),
        name='tag_post'
    ),
]