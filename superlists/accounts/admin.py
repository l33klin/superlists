from django.contrib import admin

# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'password', 'add_time', 'mod_date', 'is_active', 'is_admin')
