from django.urls import path
from users.views import DetalleEmpleadoporID

#Urls de users
urlpatterns = [
    path('<numero_empleado>', DetalleEmpleadoporID.as_view()),
    path('', DetalleEmpleadoporID.as_view(), name='home'),
]