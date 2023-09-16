from rest_framework import routers

router = routers.DefaultRouter()

# -------------------------------
import stractor.common.api.views  as symptom_api_views

router.register(r'symptom', symptom_api_views.SymptomViewSet)
# -------------------------------

