from django.urls import path
from .views import Posts, PostDetail


urlpatterns = [
    path('news', Posts.as_view(), name='home'),
    path('<int:pk>', PostDetail.as_view(), name='post')
    ]
