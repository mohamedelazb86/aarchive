from django.urls import path
from . import views

app_name='contractor'


urlpatterns = [
    path('',views.contractor,name='contractor'),
    path('add-contractor',views.add_contractor,name='add-contractor'),
    path('delete-contractor',views.delete_contractor,name='delete-contractor'),
    path('edit-contractor',views.edit_contractor,name='edit-contractor'),

    path('document_contractor',views.document_contractor,name='document-contractor'),
    # path('getcontractordata',views.getcontractordata,name='getcontractordata'),
    # path('add_document_contractor',views.add_contractor_document,name='add-document-contractor')
    path('all_documents/<int:id>',views.all_document,name='all-documents'),
    path('delete-document/<int:id>',views.delete_document,name='delete-document'),
    path('add-document',views.add_document,name='add-document'),
    
    path('document-add',views.document_add,name='document-add'),
    path('get-contractor-data',views.getcontractordata,name='get-contractor-data'),
    path('add-contractor-document',views.add_contractor_document,name='add-contractor-document'),
]
