from django.urls import path
from blog.views import *

urlpatterns = [
    path('',blog_post_list_view),
    path('retrieve/<str:post_slug>',blog_post_retrieve_view),
    path('create',blog_post_create_view),
    path('<str:post_slug>/edit',blog_post_update_view),
    path('<str:post_slug>/delete',blog_post_delete_view),
    path('<str:post_slug>/publish',blog_post_publish_view),
]