from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import CustomUser, Address, Phone
from django.utils.safestring import mark_safe


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'age', 'is_verified', 'is_staff')
    list_filter = ('is_verified', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'age', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_verified', 'is_staff')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'geo_url_link', 'country', 'city', 'city_district', 'street', 'postcode', 
        'latitude', 'longitude', 'address'
    )
    list_filter = ('country', 'city', 'city_district')
    search_fields = ('user__username', 'geo_url', 'address')
    
    fieldsets = (
        (None, {
            'fields': ('user', 'geo_url')
        }),
        ('Адресные детали', {
            'fields': ('country', 'city', 'city_district', 'street', 'postcode', 'latitude', 'longitude', 'address')
        }),
    )

    def geo_url_link(self, obj):
        """Возвращает ссылку на URL геолокации как гиперссылку."""
        if obj.geo_url:
            return mark_safe(f'<a href="{obj.geo_url}" target="_blank">Перейти к адресу</a>')
        return "-"
    
    geo_url_link.short_description = 'URL геолокации'

    readonly_fields = ('latitude', 'longitude', 'address')

    def get_readonly_fields(self, request, obj=None):
        """Определяет поля, доступные только для чтения."""
        if obj and not obj.geo_url:
            return self.readonly_fields + ('latitude', 'longitude', 'address')
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        """Запрещаем изменение модели, если отсутствует geo_url."""
        if obj and not obj.geo_url:
            return False
        return super().has_change_permission(request, obj)
    

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'phone_country',
        'phone_type',
        'phone_local',
        'phone_international',
        'phone_carrier',
        'phone_prefix',
        'phone_code'
    )
    search_fields = ('phone', 'phone_country', 'phone_type', 'phone_carrier')
    list_filter = ('phone_country', 'phone_type')
    readonly_fields = ('phone_country', 'phone_type', 'phone_local', 'phone_international', 'phone_carrier', 'phone_prefix', 'phone_code')
    





