from rest_framework.response import Response
from rest_framework.views import APIView


class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(1111111)


class CourseDetailView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(22222222)
