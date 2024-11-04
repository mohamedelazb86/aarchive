from django.shortcuts import render,redirect
from .models import Contractor
from settings.models import Sector
from django.contrib import messages
from django.http import JsonResponse
from document.models import Documents
from django.contrib import messages
from django.http import HttpResponseRedirect
from settings.models import Document_Type
from django.contrib.auth.decorators import login_required

@login_required
def contractor(request):
    contractor=Contractor.objects.all()
    sector=Sector.objects.all()

    context={
        'contractor':contractor,
        'sector':sector
    }
    return render(request,'contractor/contractor.html',context)
@login_required
def add_contractor(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']
       
        Contractor.objects.create(
            code=code,
            name=name,
            
            sector_id=sector,
            project=project,
            item=item,
            notes=notes
        )
        messages.success(request,'تم إضافة مقاول جديد بنجاح مبرووك ')
        return redirect('/contractor')
    
@login_required
def delete_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)
        contractor.delete()
        messages.success(request,'تم الحذف بنجاح مبررووك ')
        return redirect('/contractor')
    
@login_required
def edit_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)

        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']

        contractor.code=code
        contractor.name=name
        contractor.sector_id=sector
        contractor.project=project
        contractor.itrm=item
        contractor.notes=notes

        contractor.save()

        messages.success(request,'تم التعديل بنجاح')
        return redirect('/contractor')
@login_required    
def document_contractor(request):
    document_type=Document_Type.objects.all()
    context={
        'document_type':document_type
    }
    return render(request,'contractor/document_contractor.html',context)

# def getcontractordata(request):
#     code=request.GET.get('code')
#     if code:
#            try:
#             contractor = Contractor.objects.get(code=code)
#             data = {
#                 "name": contractor.name,
#                 'sector':contractor.sector.name,
#                 'project':contractor.project,
#                 'item':contractor.item,
                
                
                
#             }
#            except Contractor.DoesNotExist:
#             data = {"name": "",
#                     'sector':'غير موجود',
#                     'project':'غير موجود',
#                     'item':'غير موجود',
                    
#                     }
#     else:
#         data = {"name": "",
#                 'sector':'',
#                 'project':'',
#                 'item':'',
                
                
#                 }
    
#     return JsonResponse(data)

# def add_contractor_document(request):
#     if request.method=='POST':
#         code=request.POST['code']
#         # contractor=Contractor.objects.get(code=code)
#         contractor=get_object_or_404(Contractor,code=code)
        
#         contractor_id=contractor.id
    
#         date=request.POST['date']
#         statment=request.POST['statment']
#         document_type=request.POST['document_type']
#         file=request.FILES.get('file')

#         Documents.objects.create(
#             statment=statment,
#             file=file,
#             date=date,
#             notes='لايوجد',
#             user=request.user,
#             document_type_id=document_type,
#             contractor_id=contractor_id

#         )
#         messages.success(request,'تم لإضافة مستند بنجاح')
        
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#     return redirect('/')
#==============================================================================

# def add_contractor_document(request):
#     if request.method == 'POST':
#         code = request.POST.get('code')

#         try:
#             # الحصول على المقاول بناءً على الكود
#             contractor = Contractor.objects.get(code=code)
#         except Contractor.DoesNotExist:
#             # عرض رسالة خطأ إذا كان المقاول غير موجود
#             messages.error(request, f"خطأ: لا يوجد مقاول بهذا الكود ({code}).")
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#         # إذا كان المقاول موجود، متابعة إنشاء المستند
#         date = request.POST.get('date')
#         statment = request.POST.get('statment')
#         document_type = request.POST.get('document_type')
#         file = request.FILES.get('file')

#         # إنشاء مستند جديد وربطه بالمقاول
#         Documents.objects.create(
#             statment=statment,
#             file=file,
#             date=date,
#             notes='لا يوجد',
#             user=request.user,
#             document_type_id=document_type,
#             contractor_id=contractor.id
#         )

#         # رسالة نجاح بعد حفظ المستند
#         messages.success(request, 'تم إضافة المستند بنجاح')
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
#     # في حال كان الطلب ليس من نوع POST
#     return redirect('/')
#=========================================================================
@login_required
def all_document(request,id):
    contractor=Contractor.objects.get(id=id)
    documents=Documents.objects.filter(contractor=contractor)
    document_type=Document_Type.objects.all()
    context={
        'contractor':contractor,
        'documents':documents,
        'document_type':document_type
    }
    
    return render(request,'contractor/all_documents.html',context)
@login_required
def delete_document(request,id):
    document=Documents.objects.get(id=id)
    document.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_document(request):
    if request.method=='POST':
        code=request.POST['code']
        contractor=Contractor.objects.get(code=code)
        
        statment=request.POST['statment']
        notes=request.POST['notes']
      
        file = request.FILES.get('file')
        date=request.POST['date']
        document_type=request.POST['document_type']


        Documents.objects.create(
            statment=statment,
            file=file,
            date=date,
            notes=notes,
            user=request.user,
            document_type_id=document_type,
            contractor_id=contractor.id


        )
        messages.success(request,'مبروووك تم إضافة مستند بنحاج')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#==============================================================================
    
@login_required
def document_add(request):
    document_type=Document_Type.objects.all()
    context={
        'document_type':document_type
    }
    return render(request,'contractor/add-document.html',context)


#============================================
@login_required
def getcontractordata(request):
    code=request.GET.get('code')
    if code:
           try:
            contractor = Contractor.objects.get(code=code)
            data = {
                "name": contractor.name,
                'sector':contractor.sector.name,
                'project':contractor.project,
                'archive_code':contractor.archive_code,
                
                
                
            }
           except Contractor.DoesNotExist:
            data = {"name": "غير موجود",
                    'sector':'غير موجود',
                    'project':'غير موجود',
                    
                    'archive_code':'غير موجود',
                    
                    }
    else:
        data = {"name": "",
                'sector':'',
                'project':'',
                'archive_code':'',
                
                
                }
    
    return JsonResponse(data)

#=========================================================
@login_required
def add_contractor_document(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        try:
            # الحصول على المقاول بناءً على الكود
            contractor = Contractor.objects.get(code=code)
        except Contractor.DoesNotExist:
            # عرض رسالة خطأ إذا كان المقاول غير موجود
            messages.error(request, f"خطأ: لا يوجد مقاول بهذا الكود ({code}).")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        # إذا كان المقاول موجود، متابعة إنشاء المستند
        date = request.POST.get('date')
        statment = request.POST.get('statment')
        document_type = request.POST.get('document_type')
        file = request.FILES.get('file')
        notes=request.POST['notes']

        # إنشاء مستند جديد وربطه بالمقاول
        Documents.objects.create(
            statment=statment,
            file=file,
            date=date,
            notes=notes,
            user=request.user,
            document_type_id=document_type,
            contractor_id=contractor.id
        )

        # رسالة نجاح بعد حفظ المستند
        messages.success(request, 'تم إضافة المستند بنجاح')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    # في حال كان الطلب ليس من نوع POST
    return redirect('/')
    







            