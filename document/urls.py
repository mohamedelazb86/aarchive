from django.urls import path
from . import views

app_name='document'

urlpatterns = [
    path('<int:id>',views.add_document,name='add-document'),
    path('add',views.add,name='document-add'),
    path('all-document',views.all_document,name='all-document'),

    path('search-document-con',views.serarch_document_con,name='search-document-con'),
    path('getcontractordata',views.getcontractordata,name='get-contractor-data'),
    path('search-name',views.search_name,name='search-name'),
]
