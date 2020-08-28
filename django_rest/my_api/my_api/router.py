from api_rest.viewsets import HqViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('hq', HqViewset)
