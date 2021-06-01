from django.urls import path

from user import views

urlpatterns = [
    path('registered/', views.Registered.as_view()),

]