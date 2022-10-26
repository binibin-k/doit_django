from django.urls import path
from . import views


urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.PostList.as_view(), name="post_list"),
    # path("<int:num>/", views.single_post_page),
    path("<int:num>/", views.PostDetail.as_view(), name='post_detail'),
]