from django.urls import path,re_path, include
from .views.account import LoginView
from .views.course import CourseViewSet

urlpatterns = [
    re_path('^login/$', LoginView.as_view(), name='login_view'),
    re_path('^course/$', CourseViewSet.as_view({"get": "list"}), name='course_view'),
    re_path('course/(?P<id>\d+)/$', CourseViewSet.as_view({"get": "retrieve"}), name='coursedetail_view')
]