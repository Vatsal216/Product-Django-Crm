from rest_framework import serializers
from models import *
class MobiletSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Product
        fields = ('processor','ram','screen_size','color')


class LaptopSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Product
        fields = ('processor','ram','Hd_capacity')
    

class ProductSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Product
        fields = '__all__'
    