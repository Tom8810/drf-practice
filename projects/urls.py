from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls')),
]

'''
ViewSetを使い、Routerを使用しない場合のurlpatterns
'''
# urlpatterns = [
#   path('projects/', views.ProjectViewSet.as_view(
#     {'get': 'list',
#     'post': 'create'}
#   ), name='project-list'),
#   path('projects/<int:pk>', views.ProjectViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
#   }), name='project-detail'),
#   path('users/', views.UserViewSet.as_view({
#     'get': 'list'
#   }), name='user-list'),
#   path('users/<int:pk>', views.UserViewSet.as_view({
#     'get': 'retrieve'
#   }), name='user-detail'),
#   path('api-auth/', include('rest_framework.urls')),
# ]

'''
ViewSetを使う前のurlpatterns
'''
# urlpatterns = [
#   path('projects/', views.ProjectList.as_view(), name='project_list'),
#   path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
#   path('users/', views.UserList.as_view(), name='user_list'),
#   path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
#   path('api-auth/', include('rest_framework.urls')),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)