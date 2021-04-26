from django.urls import path, include
from .views import HQ_details, HQ_list, GenericApiView, HqViewSet, HqGenericViwSet, HqModalViwSet
from rest_framework.routers import DefaultRouter

# para funconar as rotas do Viewset api
router = DefaultRouter()
#router.register('hqs', HqViewSet, basename='hqs')
#router.register('hqs', HqGenericViwSet, basename='hqs')
router.register('hqs', HqModalViwSet, basename='hqs')

urlpatterns = [
    
    # api-based classes
    path('hqs/', HQ_list.as_view()),
    path('hqs/<int:id>/', GenericApiView.as_view()),

    # Generics api
    path('generic/hqs/', GenericApiView.as_view()),
    path('generic/hqs/<int:id>/', GenericApiView.as_view()),

    # ViewSet api / Genereic ViewSet api
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))

]