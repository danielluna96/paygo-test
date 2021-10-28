from users.serializers import (CustomUser, CustomUserSerializer)

class UserController(object):

    def __init__(self) -> None:
        super().__init__()

    def get_empleado(self, numero_empleado) -> dict:
        user = CustomUser.objects.get(numero_empleado__iexact=numero_empleado)
        if user:
            subalternos = CustomUser.objects.filter(jefe__iexact=numero_empleado)
            serialized_subalternos = []
            ventas_total = 0

            for subalterno in subalternos:
                if user.cargo != "Ejecutivo Comercial":
                    ventas_total += int(subalterno.ventas)
                serialized_subalternos.append(CustomUserSerializer(subalterno).data)

            return {
                'usuario': CustomUserSerializer(user).data,
                'ventas_total': ventas_total,
                'subalternos': serialized_subalternos
            }
        else:
            return {}