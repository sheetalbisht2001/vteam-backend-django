from rest_framework import routers

router = routers.DefaultRouter()

# -------------------------------
import stractor.common.api.views  as distributor_api_views

router.register(r'distributor', distributor_api_views.DistributorViewSet)
# -------------------------------

