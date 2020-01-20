from django.urls import path

from frontend_app import views

app_name = 'frontend'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index")
]
