from users.serializers import (CustomUser, CustomUserSerializer)

class UserController(object):

    def __init__(self) -> None:
        super().__init__()

    def get_empleado(self, numero_empleado) -> dict:
        user = CustomUser.objects.get(numero_empleado__iexact=numero_empleado)
        if user:
            usuario_serializer = CustomUserSerializer(user).data
            subalternos = CustomUser.objects.filter(jefe__iexact=numero_empleado)
            serialized_jefe = []
            if usuario_serializer["jefe"]:
                jefe = CustomUser.objects.get(numero_empleado__iexact=usuario_serializer["jefe"])
                serialized_jefe = CustomUserSerializer(jefe).data
            serialized_subalternos = []
            ventas_total = 0
            for subalterno in subalternos:
                if user.cargo != "Ejecutivo Comercial":
                    ventas_total += int(subalterno.ventas)
                serialized_subalternos.append(CustomUserSerializer(subalterno).data)

            return {
                'usuario': usuario_serializer,
                'ventas_total': ventas_total,
                'subalternos': serialized_subalternos,
                'jefe': serialized_jefe,
            }
        else:
            return {}