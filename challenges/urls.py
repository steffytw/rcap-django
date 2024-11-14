from django.urls import path
from . import views

urlpatterns = [
     path("",views.index),
    path("<int:month>/",views.mothly_challenges_by_number),
    path("<str:month>/",views.mothly_challenges, name="monthly_challenges")
]
