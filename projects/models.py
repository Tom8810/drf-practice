from django.db import models

# Create your models here.

class Project(models.Model):
  project_name = models.CharField(max_length=100)
  total_min = models.IntegerField(default=0)
  goal_min = models.IntegerField(default=0)
  deadline_day = models.DateField()
  start_date = models.DateField(auto_now_add=True)
  is_engaging = models.BooleanField(default=False)
  owner = models.ForeignKey('auth.user', related_name='projects', on_delete=models.CASCADE)

  class Meta:
    ordering = ['start_date']
