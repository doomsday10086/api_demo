from rest_framework import serializers
from ..models import CourseDetail, Course, CourseSubCategory


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    all_section = serializers.IntegerField(source="coursedetail.hours")
    section = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "order", "template_id", "teacher", "all_section", "section"]

    def get_teacher(self, obj):
        teachers = obj.coursedetail.teachers.all()
        return [{"name": teacher.name, "signature": teacher.signature, "img": teacher.image} for teacher in teachers]

    def get_section(self, obj):
        chapters = obj.coursechapters.all()
        section_list = []
        for chapter in chapters:
            sections = chapter.coursesections.all()
            for section in sections:
                a = {"name":section.name}
                a['id'] = section.id
                a['is_free'] = section.free_trail
                section_list.append(a)
                if len(section_list) == 4:

                    return section_list

        return section_list

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = "__all__"


class CourseSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubCategory
        fields = "__all__"
