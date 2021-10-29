from users.serializers import (CustomUser, CustomUserSerializer)
class UserController(object):

    def __init__(self) -> None:
        super().__init__()

    #Get empleado nos permite obtener el usuario junto con demás
    #datos requeridos para la vista
    def get_empleado(self, numero_empleado) -> dict:
        user = CustomUser.objects.get(numero_empleado__iexact=numero_empleado)
        usuario_jerarquia = 0
        if user:
            usuario_serializer = CustomUserSerializer(user).data
            usuario_jerarquia = jerarquia(usuario_serializer["cargo"])
            subalternos = CustomUser.objects.filter(jefe__iexact=numero_empleado)
            
            #Se obtiene el la jerarquía del cargo del jefe
            jefe_serialized = []
            jefe_jerarquia = 0
            if usuario_serializer["jefe"]:
                jefe = CustomUser.objects.get(
                    numero_empleado__iexact=usuario_serializer["jefe"]
                )
                jefe_serialized = CustomUserSerializer(jefe).data
                jefe_jerarquia = jerarquia(jefe_serialized["cargo"])

            #Si el usuario no es un ejecutivo comercial se suman los valores de sus
            #subalternos
            serialized_subalternos = []
            ventas_total = 0
            for subalterno in subalternos:
                if user.cargo != "Ejecutivo Comercial":
                    ventas_total += int(subalterno.ventas)
                serialized_subalternos.append(CustomUserSerializer(subalterno).data)
            #Si las ventas siguen en 0 se acude a la función recursión
            if ventas_total == 0:
                recursion(serialized_subalternos)
                for subalterno in serialized_subalternos:
                    ventas_total += int(subalterno["ventas"])
            return {
                'usuario': usuario_serializer,
                'usuario_jerarquia': usuario_jerarquia,
                'ventas_total': ventas_total,
                'subalternos': serialized_subalternos,
                'jefe': jefe_serialized,
                'jefe_jerarquia': jefe_jerarquia,
            }
        else:
            return {}
            
#Se obtiene el valor número de jerarquia para futuras comparaciones
def jerarquia(cargo):
    switch = {
        "Asistente de Gerencia":0,
        "Ejecutivo Comercial":1,
        "Subgerente Regional":2,
        "Gerente Regional":3,
        "Gerente Comercial":4,
    }
    return switch.get(cargo, 0)

#Se obtienen los valores ventas de los subalternos
def recursion(subalternos):
    for subalterno in subalternos:
        subalternos2 = CustomUser.objects.filter(jefe__iexact=subalterno["numero_empleado"])
        for subalterno2 in subalternos2:
            subalterno["ventas"] += int(subalterno2.ventas)
            subalternos3 = CustomUser.objects.filter(jefe__iexact=subalterno2.numero_empleado)
            for subalterno3 in subalternos3:
                subalterno["ventas"] += int(subalterno3.ventas)
                subalterno2.ventas += int(subalterno3.ventas)