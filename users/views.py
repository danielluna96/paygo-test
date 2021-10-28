from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import (RetrieveAPIView)
from users.controller import UserController
from django.http import JsonResponse

#from utils.rest import ApiRestUtilities

class DetalleEmpleadoporID(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        try:
            numero_empleado: int = kwargs['numero_empleado']
            controller = UserController()
            data = controller.get_empleado(numero_empleado)
            return JsonResponse(
                status=200,
                data=data
            )
        except:
            return JsonResponse(
                status=404,
                data={'error': "Usuario no encontrado",}
            )
