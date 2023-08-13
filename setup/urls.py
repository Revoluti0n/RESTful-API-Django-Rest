from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, \
    StudentEnrollmentsList, EnrollmentStudentsList

router = routers.DefaultRouter()
router.register(prefix='students', viewset=StudentsViewSet, basename='Students')
router.register(prefix='courses', viewset=CoursesViewSet, basename='Courses')
router.register(prefix='enrollments', viewset=EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('students/', students)
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments/', StudentEnrollmentsList.as_view()),
    path('course/<int:pk>/enrollments/', EnrollmentStudentsList.as_view())
]
