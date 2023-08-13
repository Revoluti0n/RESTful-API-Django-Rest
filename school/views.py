from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, \
    StudentEnrollmentsListSerializer, EnrollmentStudentsListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    Exibindo todas as matrículas.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StudentEnrollmentsList(generics.ListAPIView):
    """
    Listando as matrículas de um aluno ou aluna.
    """

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = StudentEnrollmentsListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EnrollmentStudentsList(generics.ListAPIView):
    """
    Listando os alunos ou alunas matriculados um curso.
    """

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset

    serializer_class = EnrollmentStudentsListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
