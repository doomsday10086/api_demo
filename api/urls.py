from django.urls import path,re_path, include
from .views.account import LoginView
from .views.course import CourseView, CourseDetail

urlpatterns = [
    re_path('^login/$', LoginView.as_view(), name='login_view'),
    re_path('^course/$', CourseView.as_view(), name='course_view'),
    re_path('course/(?P<id>\d+)/$', CourseDetail.as_view(), name='coursedetail_view')
]