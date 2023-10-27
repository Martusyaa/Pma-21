from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

import datetime

from .models import Task

class Task_Serializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.edited = True
        instance.time_edited = datetime.datetime.now()
        
        instance.save()
        
        return instance
    
    
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'is_completed',
            'edited',
            'time_edited',
        ]
    
# def encode():
#     model = TaskModel('test3', '333333333', True, 10)
#     model_sr = TaskSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
    