from rest_framework import serializers
from .models import Plato, Pedido


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    # Punto extra: muestra nombre y precio de cada plato dentro del pedido
    platos_detalle = PlatoSerializer(source='platos', many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos', 'platos_detalle']