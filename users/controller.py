from users.serializers import (CustomUser, CustomUserSerializer)
class UserController(object):

    def __init__(self) -> None:
        super().__init__()

    def get_empleado(self, numero_empleado) -> dict:
        user = CustomUser.objects.get(numero_empleado__iexact=numero_empleado)
        usuario_jerarquia = 0
        if user:
            usuario_serializer = CustomUserSerializer(user).data
            usuario_jerarquia = jerarquia(usuario_serializer["cargo"])
            subalternos = CustomUser.objects.filter(jefe__iexact=numero_empleado)
            jefe_serialized = []
            jefe_jerarquia = 0
            if usuario_serializer["jefe"]:
                jefe = CustomUser.objects.get(numero_empleado__iexact=usuario_serializer["jefe"])
                jefe_serialized = CustomUserSerializer(jefe).data
                jefe_jerarquia = jerarquia(jefe_serialized["cargo"])
            serialized_subalternos = []
            ventas_total = 0
            for subalterno in subalternos:
                if user.cargo != "Ejecutivo Comercial":
                    ventas_total += int(subalterno.ventas)
                serialized_subalternos.append(CustomUserSerializer(subalterno).data)
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

def jerarquia(cargo):
    switch = {
        "Asistente de Gerencia":0,
        "Ejecutivo Comercial":1,
        "Subgerente Regional":2,
        "Gerente Regional":3,
        "Gerente Comercial":4,
    }
    return switch.get(cargo, 0)