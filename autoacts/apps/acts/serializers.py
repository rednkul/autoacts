from rest_framework import serializers
from .models import Type, Act, Project, Material


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', ]


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name', 'passport']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'template']


class ActSerializer(serializers.ModelSerializer):
    act_type = TypeSerializer
    materials = MaterialSerializer
    project = ProjectSerializer

    class Meta:
        model = Act
        fields = ['act_type', 'number', 'materials', 'order_number', 'project']
