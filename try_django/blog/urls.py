from django.urls import path
from blog.views import *

urlpatterns = [
    path('',blog_post_list_view),
    path('retrieve/<str:post_slug>',blog_post_retrieve_view),
    path('create',blog_post_create_view),
    path('update',blog_post_update_view),
    path('delete',blog_post_delete_view),
]