from django.contrib import admin
from customer.models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user_ptr_id', 'username', 'email', 'is_superuser', 'phone', 'is_active']
    search_fields = ['username', 'phone', 'first_name', 'last_name']
    exclude = ['last_login',
               'is_superuser',
               'groups',
               'user_permissions',
               'is_staff',
               'is_active',
               'date_joined',
               '']

    # def save_model(self, request, obj, form, change):
    #     obj.set_password(obj.password)
    #     super().save_model(request, obj, form, change)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_address', 'state', 'city', 'zip_code', 'plaque', 'lat', 'lng']
    search_fields = ['owner_address', 'state', 'city', 'plaque']

    @staticmethod
    def owner_address(obj):
        return obj.owner.username


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
