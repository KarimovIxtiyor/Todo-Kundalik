from django.contrib import admin
from .models import Todo


@admin.register(Todo)                               # Todo ni class imizga bog`lab qo`yadi
class TodoAdmin(admin.ModelAdmin):
    model=Todo
    list_display = ['datetime','user','done']       # admin panelda todoni qaysi ustunlarini ko`rmoqchimiz

