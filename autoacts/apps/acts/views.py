from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Type, Act, Project, Material
from .serializers import TypeSerializer, ProjectSerializer, ActSerializer
# Create your views here.


class TypeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

class TypeCreateView(CreateAPIView):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

class ProjectCreateView(CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ActCreateView(CreateAPIView):
    serializer_class = ActSerializer
    queryset = Act.objects.all()