from django.urls import path
from .views import HQ_list, HQ_detail

urlpatterns = [
    path('hqs/', HQ_list),
    path('hqs/<int:pk>', HQ_detail),
]
