from django.urls import path
from . import views

app_name='settings'
urlpatterns = [
    # path('',views.index,name='index'),
    path('document_type',views.document_type,name='document-type'),
    path('add-document-type',views.add_document_type,name='add-document-type'),
    path('delete-document-type',views.delete_document_type,name='delete-document-type'),
    path('edit-document-type',views.edit_document_type,name='edit-document-type'),

    # sector
    path('sector',views.sector,name='sector'),
    path('add-sector',views.add_sector,name='add-sector'),
    path('delete-sector',views.delete_sector,name='delete-sector'),
    path('edit-sector',views.edit_sectot,name='edit-sector'),

    path('',views.dashbord),
]
