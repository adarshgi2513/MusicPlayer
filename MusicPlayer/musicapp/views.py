from django.shortcuts import render,get_object_or_404,redirect
from.models import song
from django.core.paginator import Paginator
from.forms import Dataform


# Create your views here.
def home(request):
    paginator= Paginator(song.objects.all(),1)
    page_number= request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"music.html",context)


def data_views(request):
    data_value=song.objects.all()
    return render(request,"datas.html",{'song':data_value})


def searchbar(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data_value=song.objects.filter(title__icontains=q) 
        # data_value=song.objects.filter(artist__icontains=q)  
    else:
        data_value=song.objects.all()
    context={
        'song':data_value
    } 
    return render(request,'datas.html',context)

def form(request):
    form=Dataform()
    return render(request,'forms.html',{'form':form})


def save(request):
    if request.method == 'POST':
        form = Dataform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'forms.html',{'form':form})  
        else:
            print(form.errors)  
    else:
        form = Dataform()

    return render(request, 'forms.html', {'form': form})
