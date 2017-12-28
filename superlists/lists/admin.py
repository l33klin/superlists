from django.contrib import admin

# Register your models here.


class ListAdmin(admin.ModelAdmin):
    fields = ()


class Item(admin.ModelAdmin):
    fields = ('text', 'list')

