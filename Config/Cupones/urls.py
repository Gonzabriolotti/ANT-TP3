from rest_framework import routers
from Cupones import views
from django.urls import path , include

router = routers.DefaultRouter()
router.register(r'cupones', views.CuponesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]