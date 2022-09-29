from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from .models import Type, Act, Project, Material
from .serializers import TypeSerializer, ProjectSerializer, ActSerializer, MaterialSerializer
# Create your views here.
from .service import describe_project


class TypeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

class TypeCreateView(CreateAPIView):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

class ProjectCreateView(CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            describe_project(project)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        print(request.data, *args, **kwargs)

        return self.create(request, *args, **kwargs)

class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ActCreateView(CreateAPIView):
    serializer_class = ActSerializer
    queryset = Act.objects.all()

class MaterialCreateView(CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()