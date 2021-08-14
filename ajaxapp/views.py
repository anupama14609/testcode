from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import LibraryForm
from .models import Library
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def LibraryHome(request):
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

def DeleteBook(request, id):
    if request.method == 'POST':
        book_id = Library.objects.get(pk=id)
        book_id.delete()
        return HttpResponseRedirect('/')

def UpdateBook(request, id):
    if request.method == 'POST':
        record_id = Library.objects.get(pk=id)
        updateform = LibraryForm(request.POST, instance=record_id)
        if updateform.is_valid():
            updateform.save()
    else:
        record_id = Library.objects.get(pk=id)
        updateform = LibraryForm(instance=record_id)

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