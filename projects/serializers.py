from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Project
    fields = ['id', 'project_name', 'total_min', 'goal_min', 'deadline_day', 'start_date', 'is_engaging', 'owner' ]

class UserSerializer(serializers.ModelSerializer):
  projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'projects']