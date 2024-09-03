from django.contrib import admin
from .models import Guardia, Administrador

class CustomGuardiaAdmin(admin.ModelAdmin):
    model = Guardia
    list_display = ['get_username', 'get_email', 'get_is_staff', 'get_is_superuser']
    fieldsets = (
        (None, {'fields': ('user',)}),
    )
    search_fields = ('user__username', 'user__email')
    ordering = ('user__username',)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_is_staff(self, obj):
        return obj.user.is_staff
    get_is_staff.short_description = 'Is Staff'

    def get_is_superuser(self, obj):
        return obj.user.is_superuser
    get_is_superuser.short_description = 'Is Superuser'

admin.site.register(Guardia, CustomGuardiaAdmin)

class CustomAdministradorAdmin(admin.ModelAdmin):
    model = Administrador
    list_display = ['get_username', 'get_email', 'get_is_staff', 'get_is_superuser']
    fieldsets = (
        (None, {'fields': ('user',)}),
    )
    search_fields = ('user__username', 'user__email')
    ordering = ('user__username',)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_is_staff(self, obj):
        return obj.user.is_staff
    get_is_staff.short_description = 'Is Staff'

    def get_is_superuser(self, obj):
        return obj.user.is_superuser
    get_is_superuser.short_description = 'Is Superuser'

admin.site.register(Administrador, CustomAdministradorAdmin)
