from rest_framework import routers
from .api import VarViewSet

router = routers.DefaultRouter()

router.register('api/Variables',VarViewSet, 'proyectoAPI')

urlpatterns = router.urls
