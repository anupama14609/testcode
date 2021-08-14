from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import LibraryForm
from .models import Library
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


# Create your views here.
def LibraryHome(request):
    error=""
    form = LibraryForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Details Has Been Updated.............')
        except: 
            messages.error(request, 'Something went wrong.........')
    form = LibraryForm()
    paginated_content = Library.objects.all().order_by('-timeStamp')
    content = Paginator(paginated_content.filter(publish=True), 4)
    page = request.GET.get('page')
    try:
        content = content.page(page)
    except PageNotAnInteger:
        content = content.page(1)
    except EmptyPage:
        content = content.page(content.num_pages)
    context = {
        'form':form,
        'content':content,
        'error':error,
    }
    return render(request, 'ajaxapp/library.html', context)

def DeleteBook(request, id):
    if request.method == 'POST':
        book_id = Library.objects.get(pk=id)
        book_id.delete()
        messages.error(request, 'Record has been deleted.')
        return HttpResponseRedirect('/')

def UpdateBook(request, id):
    messages = "Details Has Been Updated............."
    if request.method == 'POST':
        record_id = Library.objects.get(pk=id)
        updateform = LibraryForm(request.POST, instance=record_id)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, 'Details Has Been Updated.............')
    else:
        record_id = Library.objects.get(pk=id)
        updateform = LibraryForm(instance=record_id)
        messages.success(request, 'Details Has Been Updated.............')

    context = { 'form': updateform}
    return render(request, 'ajaxapp/updatebook.html', context)

def home(request):
    error=""
    form = LibraryForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except: 
            error = "Something went wrong..........."
    form = LibraryForm()
    paginated_content = Library.objects.all().order_by('-timeStamp')
    content = Paginator(paginated_content.filter(publish=True), 4)
    page = request.GET.get('page')
    try:
        content = content.page(page)
    except PageNotAnInteger:
        content = content.page(1)
    except EmptyPage:
        content = content.page(content.num_pages)
    context = {
        'form':form,
        'content':content,
        'error':error,
    }
    return render(request, 'ajaxapp/library.html', context)