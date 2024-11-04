from django.urls import path
from . import views

app_name='mail'

urlpatterns = [
    path('',views.document_mail,name='document-mail'),
    path('add-document-mail',views.add_document,name='add-document-mail'),
    path('delete-document-mail',views.delete_document,name='delete-document-mail'),

    # user_document
    path('user-document',views.user_document,name='user-document'),
    path('add-user-document',views.add_user_document,name='add-user-document'),
    path('delete-user-document',views.delete_user_document,name='delete-user-document'),
    
]
