from django.urls import path
from users.views import DetalleEmpleadoporID

urlpatterns = [
    path('user/<numero_empleado>', DetalleEmpleadoporID.as_view()),
    path('', DetalleEmpleadoporID.as_view(), name='home'),
]