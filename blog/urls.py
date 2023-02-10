from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="blog"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('single/<slug:slug>', views.single, name="single"),
    path('aboutus/', views.aboutus, name="aboutus"),
]

'''
urlpatterns = [path('home/', TemplateView.as_view(template_name="home.html"))]
'''