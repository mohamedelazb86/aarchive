from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Document_Type,Sector
from document.models import Documents

# Create your views here.

def index(request):
    return render(request,'settings/index.html',{})


@login_required
def document_type(request):
    document_type=Document_Type.objects.all()
    context={
        'document_type':document_type
    }
    return render(request,'settings/document_type.html',context)


@login_required
def add_document_type(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Document_Type.objects.create(
            code=code,
            name=name,
            notes=notes
        )
        messages.success(request,'تم إضافة نوع مستند جديد بنجاح')
        return redirect('/document_type')
    
@login_required
def delete_document_type(request):
    if request.method=='POST':
        document_type_id=request.POST['id']
        document_type=Document_Type.objects.get(id=document_type_id)
        document_type.delete()
        messages.success(request,'تم الحذف  بنجاح مبرووك ')
        return redirect('/document_type')

@login_required    
def edit_document_type(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        document_type_id=request.POST['id']
        document_type=Document_Type.objects.get(id=document_type_id)

        document_type.code=code
        document_type.name=name
        document_type.notes=notes

        document_type.save()

        messages.success(request,'تم التعديل بنجاح ')
        return redirect('/document_type')
    


@login_required
def sector(request):
    sector=Sector.objects.all()
    context={
        'sector':sector
    }
    return render(request,'settings/sector.html',context)


@login_required
def add_sector(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Sector.objects.create(
            code=code,
            name=name,
            notes=notes
        )
        messages.success(request,'تم إضافة قطاع جديد بنجاح')
        return redirect('/sector')
    

    
@login_required
def delete_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)
        sector.delete()
        messages.success(request,'تم الحذف  بنجاح مبرووك ')
        return redirect('/sector')
    

    
@login_required    
def edit_sectot(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)

        sector.code=code
        sector.name=name
        sector.notes=notes

        sector.save()

        messages.success(request,'تم التعديل بنجاح ')
        return redirect('/sector')
    
def dashbord(request):
        
    # Group orders by status and count them
    document_sector_counts = Documents.objects.values('contractor__sector__name').annotate(count=Count('id'))

    # Prepare data for Chart.js
    sector_labels = [entry['contractor__sector__name'] for entry in document_sector_counts]
    sector_data = [entry['count'] for entry in document_sector_counts]

    context = {
        'sector_labels' : sector_labels,
        'sector_data' : sector_data,
    }

    return render(request,'settings/dashbord.html',context)

