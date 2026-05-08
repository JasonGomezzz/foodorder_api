from rest_framework import viewsets, filters
from .models import Plato, Pedido
from .serializers import PlatoSerializer, PedidoSerializer


class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'categoria']


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado']