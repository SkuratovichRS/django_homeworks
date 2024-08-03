from rest_framework import serializers

from logistic.models import Stock, StockProduct, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'stock', 'product', 'quantity', 'price']
        read_only_fields = ['id', 'stock']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']
        read_only_fields = ['id']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        StockProduct.objects.bulk_create([
            StockProduct(stock=stock,
                         product=position['product'],
                         quantity=position['quantity'],
                         price=position['price'], ) for position in positions
        ])

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                quantity=position['quantity'],
                price=position['price'],
            )

        return stock
