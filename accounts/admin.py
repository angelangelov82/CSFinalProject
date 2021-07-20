from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Django custom User login Model


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')#Django admin site to show these fields of user data
    list_display_links = ('email', 'first_name', 'last_name')#these links allow you to see these fields as links and access user data page
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',) # disending order of records

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
