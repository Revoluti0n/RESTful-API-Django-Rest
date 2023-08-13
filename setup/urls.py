from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix='students', viewset=StudentsViewSet, basename='Students')
router.register(prefix='courses', viewset=CoursesViewSet, basename='Courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('students/', students)
    path('', include(router.urls))
]
