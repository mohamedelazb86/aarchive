from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Sector,Document_Type

class Sectoradmin(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']

    summernote_fields = ('notes',)
    
class DocumentType(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']

    summernote_fields = ('notes',)


admin.site.register(Sector,Sectoradmin)
admin.site.register(Document_Type,DocumentType)
