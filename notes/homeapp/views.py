from django.shortcuts import render,redirect
from homeapp.models import *
from authapp.models import *
from authapp.decorator import login_required_custom1
from django.core.paginator import Paginator

@login_required_custom1
def home_create_notes(request):

    user_id=request.session.get('user_id')
    user= User.objects.get(id=user_id)
    
    if request.method=='POST':
        
        title=request.POST.get('title')
        description=request.POST.get('description')

        Notes.objects.create(user=user,title=title,description=description)
        return redirect('home_create_notes')

    search=request.GET.get('search')    
    notes=Notes.objects.filter(user=user,is_delete=False)

    if search:
        notes=Notes.objects.filter(user=user,is_delete=True,title__icontains=search)

    else:
        notes=Notes.objects.filter(user=user,is_delete=False)

    paginator = Paginator(notes,5)
    page_number=request.GET.get('page')

    notes=paginator.get_page(page_number)

    return render(request,'home_system.html',context={'notes':notes,'user':user})

def home_delete_note(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    note=Notes.objects.get(id=id,user=user)
    note.is_delete=True
    note.save()
    return redirect('home_create_notes')

def home_update_note(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    note=Notes.objects.get(id=id,user=user)

    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')

        note.title=title
        note.description=description
        note.save()

        return redirect('home_create_notes')
    
    return render(request,'update_system.html',context={'note':note})

def add_favourites(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    note=Notes.objects.get(id=id,user=user)

    note.is_favourite = True
    note.save()
    return redirect('home_create_notes')

def remove_favourites(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    note=Notes.objects.get(id=id,user=user)

    note.is_favourite = False
    note.save()
    return redirect('home_create_notes')


def permanent_delete(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    deleted_note=Notes.objects.get(id=id,user=user,is_delete=True)
    deleted_note.delete()
    return redirect('recycle_bin')
    

def restore_note(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    deleted_note=Notes.objects.get(id=id,user=user,is_delete=True)
    
    deleted_note.is_delete=False
    deleted_note.save()
    return redirect('recycle_bin')

def recycle_bin(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    deleted_notes=Notes.objects.filter(user=user,is_delete=True)

    return render(request,'recycle_bin.html',context={'deleted_notes':deleted_notes})
    
    



    






