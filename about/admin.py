from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteInlineModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteInlineModelAdmin):
    summernote_fields = ('content',)
