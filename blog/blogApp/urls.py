
from django.urls import path
from .views import PostDetailAPIView,PostDeleteAPIView,PostCreateAPIView,PostListAPIView,UserDetailAPIView

urlpatterns = [
    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
    path('post/<int:pk>/delete/', PostDeleteAPIView.as_view()),
    path('post/create/', PostCreateAPIView.as_view()),
    path('user/<int:pk>/', UserDetailAPIView.as_view()),

]
