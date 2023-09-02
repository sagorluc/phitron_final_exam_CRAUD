from django.shortcuts import render, redirect, get_object_or_404
from crud_app.models import CrudModel
from crud_app.forms import CrudFrom, Update
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def show_crud(request):
    crud = CrudModel.objects.all()
    context = {'cruds': crud}
    return render(request, 'show_crud.html', context)

@login_required
def create_crud(request):
    form = CrudFrom()
    if request.method == 'POST':
        form = CrudFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_crud')
    else:
        form = CrudFrom()
    return render(request, 'create_post.html', {'forms': form})

@login_required
def update_crud(request, id):
    get_id = CrudModel.objects.get(pk = id)
    get_ins = Update(instance= get_id)
    
    # update data
    if request.method == 'POST':
        form = Update(request.POST, request.FILES, instance= get_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your data is updated')
            return redirect('show_crud')

    return render(request, 'update_crud.html', {'forms': get_ins})
    
@login_required    
def delete_crud(request, id):
    obj = CrudModel.objects.get(pk= id).delete()
    return redirect('show_crud')

@login_required
def more_info(request, id):
    get_obj = get_object_or_404(CrudModel, pk = id)
    return render(request, 'more_info.html', {'info': get_obj})

@login_required
def search_item(request):
    keyword = request.GET.get('keyword', '')
    print('line 53',keyword)
    persons = []

    if keyword:
        persons = CrudModel.objects.filter(Q(name__icontains=keyword) | Q(course__icontains= keyword))
        
    print('line 59 ',persons)

    return render(request, 'search.html', {'keyword': keyword, 'persons': persons})    


        
    