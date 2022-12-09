from django.urls import path
from comment import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()) 
]
