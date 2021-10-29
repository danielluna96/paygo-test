from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.generics import (RetrieveAPIView)
from users.controller import UserController,jerarquia

#Clase vista encargada de mostrar los datos de usuario
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

            #Verificación de la jerarquia del usuario logueado con el solicitado
            usuario_logueado_jerarquia = jerarquia(request.user.cargo)
            if(usuario_logueado_jerarquia <= data["usuario_jerarquia"]):
                if(request.user.numero_empleado != data["usuario"]["numero_empleado"]):
                    return redirect('home')

            context = {
                "usuario": data["usuario"],
                "usuario_logueado_jerarquia": usuario_logueado_jerarquia,
                "subalternos": data["subalternos"],
                "ventas_total": data["ventas_total"],
                "jefe": data["jefe"],
                "jefe_jerarquia": data["jefe_jerarquia"]
            }
            return render(request, 'user.html', context)
        except:
            return redirect('../accounts/login/')


