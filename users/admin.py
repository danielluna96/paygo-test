from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'date_joined', 'is_staff')
	search_fields = ('email',)
	readonly_fields=('id', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)