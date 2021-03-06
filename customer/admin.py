from django.contrib import admin
from customer.models import *


class AddressInline(admin.StackedInline):
    model = Address
    list_display = [
        'id',
        'owner_address',
        'state', 'city',
        'zip_code',
        'plaque',
        'lat',
        'lng'
    ]
    search_fields = [
        'owner_address',
        'state', 'city',
        'plaque'
    ]

    @staticmethod
    def owner_address(obj):
        return obj.owner.username

    fieldsets = [
        ("required",
         {'fields': [
             'owner',
             'state',
             'city',
             'zip_code',
             'plaque',
         ]}),
        ('optional',
         {'fields': [
             'detail',
             'lat',
             'lng'
         ]
         })
    ]
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'user_ptr_id',
        'username',
        'email',
        'is_superuser',
        'phone',
        'is_active',
    ]
    search_fields = [
        'username',
        'phone',
        'first_name',
        'last_name'
    ]

    fieldsets = [
        ("required",
         {'fields': [
             'username',
             'phone',
             'password'
         ]}),
        ("optional",
         {'fields': [
             'first_name',
             'last_name',
             'email',
             'customer_image'
         ]})
    ]

    inlines = [AddressInline]

    list_filter = [
        'username',
        'phone'
    ]

# def save_model(self, request, obj, form, change):
#     obj.set_password(obj.password)
#     super().save_model(request, obj, form, change)


admin.site.register(Customer, CustomerAdmin)
