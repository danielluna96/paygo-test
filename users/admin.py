from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

#Se realiza la modificación del admin para poder adicionar y editar usuarios
#a través de un superuser
class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'date_joined', 'is_staff')
	search_fields = ('email',)
	readonly_fields=('id', 'date_joined')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = (
        (('User'), {'fields': ('email','nombre','apellido_uno','apellido_dos',
		'cedula','fecha_nacimiento','genero','fecha_ingreso','numero_empleado',
		'cargo','jefe','zona', 'municipio','departamento','ventas','imagen',
		'celular',)}),
        (('Permissions'), {'fields': ('is_active','is_staff')}),
    )

	add_fieldsets = (
		(None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2','nombre','apellido_uno',
            'apellido_dos','cedula','fecha_nacimiento','genero','fecha_ingreso',
            'numero_empleado','cargo','jefe','zona', 'municipio','departamento',
            'ventas','imagen','celular',),
			} 
	    ),
    )

admin.site.register(CustomUser, CustomUserAdmin)