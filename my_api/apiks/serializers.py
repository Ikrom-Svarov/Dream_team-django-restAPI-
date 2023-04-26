from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task





class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TaskSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Task 
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = UserSerializers(instance.owner).data  
        return representation
    