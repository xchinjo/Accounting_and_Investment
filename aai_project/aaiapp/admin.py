from django.contrib import admin
from .models import AiModel

class AiAdmin(admin.ModelAdmin):
    list_display = ("name","crdt")
    list_filter = ("crdt",)

admin.site.register(AiModel, AiAdmin)