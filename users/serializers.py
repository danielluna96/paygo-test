from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'nombre',
            'apellido_uno',
            'apellido_dos',
            'cedula',
            'fecha_nacimiento',
            'genero',
            'fecha_ingreso',
            'numero_empleado',
            'cargo',
            'jefe',
            'zona',
            'municipio',
            'departamento',
            'ventas',
            'imagen',
            'celular',
        ]

    def create(self, validated_data):
        user_password = validated_data['password']
        user = CustomUser.objects.create(password= make_password(user_password), **validated_data)
        user.username = validated_data['email']
        user.save()
        return user

    def delete(self, instance):
        user = CustomUser.objects.get(instance)
        user.delete()

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user