from django.shortcuts import redirect, render
from lists.models import Item, List
#from django.http import HttpResponse
# Create your views here.
def home_page(request):
    '''домашняя страница'''
    return render(request, 'home.html')

def home_page1(request):
    '''домашняя страница'''
    return render(request, 'home.html')

def new_list(request):
    '''новый список'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    '''представление списка'''
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def add_item(request, list_id):
    '''добавить элемент'''
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
