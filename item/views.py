from django.contrib.auth.decorators import login_required
from django.db.models import Q 

from django.shortcuts import render, get_object_or_404, redirect

from .forms import EditItemForm, NewItemForm
from item.models import Category, Item

# /////////////////////////////////////////////////
from django.http import JsonResponse
from .models import Item
from .serializers import Dserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# /////////////////////////////////////////////////


@api_view(['GET', 'POST'])
def Item_list(request ,format=None):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = Dserializer(items, many=True)
        #return JsonResponse({'items':serializer.data}, safe=False)
        return Response(serializer.data) 
    if request.method == 'POST':
        serializer = Dserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def item_detail(request,id,format = None):
    try:
       item = Item.objects.get(pk = id)
    except Item.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Dserializer(item)
        return Response(serializer.data) 
    if request.method == 'PUT':
        serializer = Dserializer(item,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
# /////////////////////////////////////////////////

def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_Sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) |Q(description__icontains=query) )


    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(request, pk):
    item =  get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category = item.category, is_Sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            # obj = Item(category=item.category,name=item.name,description=item.description,price=item.price,image=item.image,is_Sold=item.is_Sold,created_by= 1,created_at=item.created_at)
            # obj.save(using='database2')
            # if(item.price > 100):
            #     item.save(using='database2')
            # else:
            item.save()
                

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })