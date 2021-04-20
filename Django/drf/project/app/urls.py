from django.urls import path
from .views import HQ_details, HQ_list, GenericApiView

urlpatterns = [
    path('hqs/', HQ_list.as_view()),
    path('hqs/<int:id>/', GenericApiView.as_view()),
    path('generic/hqs/', GenericApiView.as_view()),
    path('generic/hqs/<int:id>/', GenericApiView.as_view()),
]