from django.shortcuts import render,redirect,get_object_or_404
from django.views import  View
from .models import Davlat

class ListView(View):
    def get(self,request):
        davlatlar=Davlat.objects.all()
        return render(request,'index.html',{'davlatlar':davlatlar})


class DetailView(View):
    def get(self,request,pk):
        davlat=get_object_or_404(Davlat,id=pk)
        return render(request,'detail.html',{'davlat':davlat})

class CreateView(View):
    def get(self,request):
        return render(request,'create.html')

    def post(self,request):
        davlat=Davlat.objects.create(
            nomi=request.POST.get('nomi'),
            poytaxti=request.POST.get('poytaxti'),
            aholisi=request.POST.get('aholisi'),
            mustaqillik_yili=request.POST.get('mustaqillik_yili'),
            desc=request.POST.get('desc'),
        )
        davlat.save()
        return redirect('index')


class UpdateView(View):
    def get(self,request,pk):
        davlat=get_object_or_404(Davlat,id=pk)
        return render(request,'update.html',{'davlat':davlat})

    def post(self,request,pk):
        davlat=get_object_or_404(Davlat,id=pk)
        davlat.nomi=request.POST.get('nomi')
        davlat.poytaxti=request.POST.get('poytaxti')
        davlat.aholisi=request.POST.get('aholisi')
        davlat.mustaqillik_yili=request.POST.get('mustaqillik_yili')
        davlat.desc=request.POST.get('desc')
        davlat.save()
        return redirect('index')


class DeleteView(View):
    def get(self,request,pk):
        davlat=get_object_or_404(Davlat,id=pk)
        davlat.delete()
        return redirect('index')























