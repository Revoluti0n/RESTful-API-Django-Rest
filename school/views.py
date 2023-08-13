from rest_framework import viewsets
from school.models import Student, Course
from school.serializer import StudentSerializer, CourseSerializer


# python manage.py runserver
# http://127.0.0.1:8000/students/

# from django.http import JsonResponse
# def students(request):
#     if request.method == 'GET':
#         student = {'id': 1, 'name': 'Kelvyn Xavier'}
#         return JsonResponse(data=student)


class StudentsViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos e alunas.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
