from rest_framework.routers import DefaultRouter
from .views import PlatoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'platos', PlatoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = router.urls