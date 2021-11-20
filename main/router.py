from rest_framework.routers import DefaultRouter
from main.views import TaskViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')
router.register(r'image', ImageViewSet, basename='image')
urlpatterns = router.urls
