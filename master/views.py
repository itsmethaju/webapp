from .forms import *
from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def home(request):
    service =Service.objects.all()
    resume =Resume.objects.all()
    testimonials =Testimonials.objects.all()
    logos =Logos.objects.all()
    y_video =VideoPresentation.objects.all()
    return render(request,'index5.html',{'service':service,'resume':resume,'testimonials':testimonials,'logos':logos,'y_video':y_video})

def protfolio(request):
    protfolio =Portfolio.objects.all()
    gallery =Gallery.objects.all()
    det_opt= Detail_opations.objects.all()
    return render(request,'portfolio5.html',{'protfolio':protfolio,'gallery':gallery,'det_opt':det_opt})

def protfolio_detial(request,pk):
    protfolio = Portfolio.objects.get(pk=pk)

    return render(request, 'portfolio-single6.html', {'pr': protfolio,})

def blog(request):
    category =BlogCatgory.objects.all()
    tages = BlogTages.objects.all()
    blog =Bloge.objects.all()
    return render(request,'blog.html',{'blog':blog,'cat':category,'tages':tages})


def blog_detail(request,pk):
    blog = Bloge.objects.get(pk=pk)

    return render(request, 'blog-single.html', {'blog': blog,})


def team(request):
    team =Team.objects.all()
    return render(request,'team.html',{'team':team})

    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contacts.html', context)

def sub_view(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = SubForm()
    context = {'form': form}
    return render(request, 'base.html', context)

