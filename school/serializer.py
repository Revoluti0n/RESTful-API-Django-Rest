from rest_framework import serializers
from school.models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']  # Definir os dados que serão disponibilizados pela API


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Disponibilizar todos os dados pela API


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []  # Outra forma de disponibilizar todos os dados pela API


class StudentEnrollmentsListSerializer(serializers.ModelSerializer):
    """
    Serializa todas as matrículas de um determinado aluno.
    """

    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    @staticmethod
    def get_period(obj):
        return obj.get_period_display()


class EnrollmentStudentsListSerializer(serializers.ModelSerializer):
    """
    Serializa todos os alunos ou alunas matículados em um curso.
    """

    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Enrollment
        fields = ['student_name']
