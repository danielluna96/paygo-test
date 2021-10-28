from django.urls import path
from users.views import *

urlpatterns = [
    path('get/<numero_empleado>', DetalleEmpleadoporID.as_view()),
]