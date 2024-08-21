from django.urls import path
from . import views

app_name = "familiares"

urlpatterns = [
    path('', views.index, name="index"),
    path('pais/list/', views.pais_list, name="pais_list"),
    path('familiar/list/', views.familiares_list, name="familiar_list"),
]
