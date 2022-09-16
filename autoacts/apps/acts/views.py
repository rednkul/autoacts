from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Type, Act, Project, Material
from .serializers import TypeSerializer, ProjectSerializer, ActSerializer, MaterialSerializer
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

    # def post(self, request):
    #     print(request)
    #     project
    #     return Response({'ok':'ok'})

class ActCreateView(CreateAPIView):
    serializer_class = ActSerializer
    queryset = Act.objects.all()

class MaterialCreateView(CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()