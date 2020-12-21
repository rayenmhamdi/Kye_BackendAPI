from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from access.models import Profile, Store, Licence, KyeUser

admin.site.register(Profile)
admin.site.register(KyeUser)
admin.site.register(Store)
admin.site.register(Licence)


class CustomUserAdmin(UserAdmin):
    model = KyeUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)