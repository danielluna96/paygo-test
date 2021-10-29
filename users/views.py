from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.generics import (RetrieveAPIView)
from users.controller import UserController

class DetalleEmpleadoporID(LoginRequiredMixin, RetrieveAPIView):  
    login_url = ''
    redirect_field_name = ''
    def get(self, request, *args, **kwargs):
        try:
            if 'numero_empleado' in kwargs:
                numero_empleado: int = kwargs['numero_empleado']
            else:
                if request.user.is_authenticated:
                    numero_empleado: int = request.user.numero_empleado
            controller = UserController()
            data = controller.get_empleado(numero_empleado)
            context = {
                "usuario": data["usuario"],
                "subalternos": data["subalternos"],
                "ventas_total": data["ventas_total"],
                "jefe": data["jefe"]
            }
            return render(request, 'user.html', context)
        except:
            return redirect('../accounts/login/')           