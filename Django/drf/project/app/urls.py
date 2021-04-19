from django.urls import path
from .views import HQ_details, HQ_list

urlpatterns = [
    path('hqs/', HQ_list.as_view()),
    path('hqs/<int:id>', HQ_details.as_view()),
]
