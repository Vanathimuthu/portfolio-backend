from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

router.register(
    "skills",
    SkillViewSet
)

urlpatterns = router.urls