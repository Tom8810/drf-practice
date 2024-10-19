from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Project
from projects.serializers import ProjectSerializer, UserSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from projects.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

'''
以下は抽象化したユーザーのクラスベースビュー
'''
# class UserList(generics.ListAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

'''
以下は抽象化したクラスベースビュー
'''
# class ProjectList(generics.ListCreateAPIView):
#   queryset = Project.objects.all()
#   serializer_class = ProjectSerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#   def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)

# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Project.objects.all()
#   serializer_class = ProjectSerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

'''
以下はミックスインを使用したクラスベースビュー
'''
# class ProjectList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#   queryset = Project.objects.all()
#   serializer_class = ProjectSerializer

#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)
  
#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)

# class ProjectDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#   queryset = Project.objects.all()
#   serializer_class = ProjectSerializer

#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)
  
#   def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)
  
#   def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)


'''
以下は最も具体的なクラスベースビュー
'''
# class ProjectList(APIView):
#   def get(self, request, format=None):
#     data = Project.objects.all()
#     serializer = ProjectSerializer(data, many=True)
#     return Response(serializer.data)
  
#   def post(self, request, format=None):
#     serializer = ProjectSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProjectDetail(APIView):
#   def get_object(self, pk):
#     try:
#       return Project.objects.get(pk=pk)
#     except Project.DoesNotExist:
#       raise Http404

#   def get(self, request, pk, format=None):
#     project = self.get_object(pk=pk)
#     serialzier = ProjectSerializer(project)
#     return Response(serialzier.data)
  
#   def put(self, request, pk, format=None):
#     project = self.get_object(pk=pk)
#     serializer = ProjectSerializer(project, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, pk, format=None):
#     project = self.get_object(pk=pk)
#     project.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


'''
以下は関数ベースビュー
'''
# @api_view(['GET', 'POST'])
# def project_list(request, format=None):
#   if request.method == 'GET':
#     data = Project.objects.all()
#     serializer = ProjectSerializer(data, many=True)
#     return Response(serializer.data)
  
#   elif request.method == 'POST':
#     serializer = ProjectSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def project_detail(request, pk, format=None):
#   try:
#     project = Project.objects.get(pk=pk)
#   except Project.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
  
#   if request.method == 'GET':
#     serializer = ProjectSerializer(project)
#     return Response(serializer.data)
  
#   elif request.method == 'PUT':
#     serializer = ProjectSerializer(project, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   elif request.method == 'DELETE':
#     project.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)