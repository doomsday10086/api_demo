from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from api.utils.baseresponse import BaseResponse
from api import models
from api.utils import serializer


class CourseViewSet(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        # 获取所有普通课程
        ret = BaseResponse()
        course_queryset = models.Course.objects.filter(degree_course=None)
        ser = serializer.CourseSerializer(instance=course_queryset, many=True)
        ret.data = ser.data
        return Response(ret.dict)

    def retrieve(self, request, *args, **kwargs):
        # 普通课程详情展示
        return Response(2222222)
