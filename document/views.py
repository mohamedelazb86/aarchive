from django.shortcuts import render
from settings.models import Document_Type
from contractor.models import Contractor
from .models import Documents
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import date,datetime
from django.core.exceptions import ValidationError
from settings.models import Sector,Document_Type
from django.http import JsonResponse
from django.http import HttpResponseRedirect

@login_required
def add_document(request,id):
    document_type=Document_Type.objects.all()
    contractor=Contractor.objects.get(id=id)

    context={
        'document_type':document_type,
        'contractor':contractor
    }

    return render(request,'document/add_document.html',context)

@login_required
def add(request):
    if request.method=='POST':
        code=request.POST['code']
        contractor=Contractor.objects.get(code=code)
        contractor_id=contractor.id
        date=request.POST['date']
        statment=request.POST['statment']
        document_type=request.POST['document_type']
        file=request.FILES.get('file')
        Documents.objects.create(
            statment=statment,
            file=file,
            date=date,
            notes='لايوجد دائما',
            user=request.user,
            document_type_id=document_type,
            contractor_id=contractor_id


        )
        messages.success(request,'تم لإضافة مستند بنجاح')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
@login_required
def con_documents_list(request, pk) :
    documents= Documents.objects.filter(contractor_id=pk)

    context = {
         'documents': documents
    }

    return render(request,'document/con_documents.html',context)

@login_required
def all_document(request):
    document_type=Document_Type.objects.all()
    #documents = Documents.objects.none()  # تعيين documents كقائمة فارغة كقيمة ابتدائية
    documents = Documents.objects.all()  # 
    if request.method=='POST':
        date_from=request.POST['date_from']
        date_to=request.POST['date_to']
        documenttype=request.POST['document_type']

        if date_from:
            date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
        else:
            date_from = date(2007, 1, 1)  # تعيين قيمة افتراضية لتاريخ البداية

        if date_to:
            date_to = datetime.strptime(date_to, "%Y-%m-%d").date()
        else:
            date_to = date.today()  # تعيين قيمة افتراضية لتاريخ النهاية

        if date_from > date_to:
            messages.error(request, "تاريخ البداية لا يمكن أن يكون بعد تاريخ النهاية.")
        else:
            # جلب الوثائق بين التاريخين إذا كان النطاق صحيحاً
            documents = Documents.objects.filter(date__range=(date_from, date_to),document_type=documenttype)


    
    context={
        'document_type':document_type,
        'documents':documents
    }
    return render(request,'document/all_document.html',context)


@login_required
def serarch_document_con(request):
    contractor=Contractor.objects.all()
    sector=Sector.objects.all()
    document_type=Document_Type.objects.all()
    documents=Documents.objects.all()

    contractor_id=request.POST.get('id')
    documenttype=request.POST.get('document_type')
    date_from=request.POST.get('date_from')
    date_to=request.POST.get('date_to')


    if request.method=='POST':
       

        if date_from:
            date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
        else:
            date_from = date(2007, 1, 1)  # تعيين قيمة افتراضية لتاريخ البداية

        if date_to:
            date_to = datetime.strptime(date_to, "%Y-%m-%d").date()
        else:
            date_to = date.today()  # تعيين قيمة افتراضية لتاريخ النهاية

        if date_from > date_to:
            messages.error(request, "تاريخ البداية لا يمكن أن يكون بعد تاريخ النهاية.")

        if not contractor_id:
            messages.error(request,'لم يتم اختيار المقاول')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                        
        
        
        if documenttype == 'all':
            documents = Documents.objects.filter(date__range=(date_from, date_to),contractor_id=contractor_id)
        else:
            documents = Documents.objects.filter(date__range=(date_from, date_to),document_type_id=documenttype,contractor_id=contractor_id)


    context={
        'contractor':contractor,
        'sector':sector,
        'document_type':document_type,
        'documents':documents
    }
    return render(request,'document/search_document_cont.html',context)


@login_required
def getcontractordata(request):
    code=request.GET.get('code')
    if code:
           try:
            contractor = Contractor.objects.get(code=code)
            data = {
                "name": contractor.name,
                "id": contractor.id,
               
                
                
                
            }
           except Contractor.DoesNotExist:
            data = {"name": "غير موجود",
                    "id": "",
                    
                    
                    }
    else:
        data = {"name": "",
                "id": "",
               
                
                
                }
    
    return JsonResponse(data)

def search_name(request):
    sectors = Sector.objects.all()
    contractors = None
    

    if request.method == 'POST':
        search_by = request.POST.get('rdio')
        sector = request.POST.get('sector')
        code = request.POST.get('code', '').strip()
        name = request.POST.get('name', '').strip()

        print(search_by)

        if search_by == 'code_value' and code:
            if sector == 'all' :
                contractors = Contractor.objects.filter(code=code)
            else :
                contractors = Contractor.objects.filter(code=code,sector=sector)
        elif search_by == 'name_value' and name:
            if sector == 'all' :
                contractors = Contractor.objects.filter(name=name)
            else :
                contractors = Contractor.objects.filter(name=name,sector=sector)
        else :
            contractors = None

    context = {
        'sectors': sectors,
        'contractors': contractors,
    }
    return render(request, 'document/search_name.html', context)