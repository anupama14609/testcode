from django.contrib import admin
from .models import Library

# Register your models here.
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
        list_display = ('name','price','pages',)
        list_per_page= 10
        search_fields = ('name',)


