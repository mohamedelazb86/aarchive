from django.shortcuts import render,redirect
from .models import Mail,User_Document
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def document_mail(request):
    document_mail=Mail.objects.all()
    context={
        'document_mail':document_mail
    }
    return render(request,'mail/document_mail.html',context)
@login_required
def add_document(request):
    if request.method=='POST':
        statment=request.POST['statment']
        document_type=request.POST['document_type']
        notes=request.POST['notes']
        date=request.POST['date']
        file=request.FILES.get('file')

        Mail.objects.create(
            statment=statment,
            document_type=document_type,
            notes=notes,
            date=date,
            file=file
        )
        messages.success(request,'تم إضافة المذكرة بنجاح')
        return redirect('/mail/')
@login_required
def delete_document(request):
    if request.method=='POST':
        document_id=request.POST['id']
        document_mail=Mail.objects.get(id=document_id)
        document_mail.delete()
        messages.success(request,'تم الحذف بنجاح')
        return redirect('/mail/')
@login_required    
def user_document(request):
    user_document=User_Document.objects.all()
    context={
        'user_document':user_document
    }
    return render(request,'mail/user_document.html',context)
@login_required
def add_user_document(request):
    if request.method=='POST':
        statment=request.POST['statment']
        document_type=request.POST['document_type']
        notes=request.POST['notes']
        date=request.POST['date']
        file=request.FILES.get('file')

        User_Document.objects.create(
            statment=statment,
            document_type=document_type,
            notes=notes,
            date=date,
            file=file,
            user=request.user
        )
        messages.success(request,'تم إضافة المذكرة بنجاح')
        return redirect('/mail/user-document')
@login_required  
def delete_user_document(request):
    if request.method=='POST':
        document_id=request.POST['id']
        document_mail=User_Document.objects.get(id=document_id)
        document_mail.delete()
        messages.success(request,'تم الحذف بنجاح')
        return redirect('/mail/user-document')



