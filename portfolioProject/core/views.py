from core.models import AboutUs, HomePageTitleAndExtra,HomePageTopSlider, HomePageWeComplete,HomePageYouGet,OurWorksSection,OurWorks, TeamMember
from django.shortcuts import redirect, render
from .forms import ContactModelForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home_view(request):
    hpte = HomePageTitleAndExtra.objects.last()
    hpts = HomePageTopSlider.objects.all()
    hpyg = HomePageYouGet.objects.all()
    hpwc = HomePageWeComplete.objects.all()
    context = {
        'hpte':hpte,
        'hpts':hpts,
        'hpyg':hpyg,
        'hpwc':hpwc
    }
    return render(request,'core/home.html',context)


# def service_view(request):
#     return render(request,'core/service.html')


def works_view(request):
    sections = OurWorksSection.objects.all()
    context = {
        'sections':sections
    }
    return render(request,'core/works.html',context)


def aboutus_view(request):
    obj = AboutUs.objects.last()
    return render(request,'core/aboutus.html',{'obj':obj})


def contactus_view(request):
    form = ContactModelForm()
    context = {'contact_form': form}
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message submission successful')
            return redirect('contactus')
    return render(request,'core/contactus.html',context)


def teams_view(request):
    members = TeamMember.objects.all()
    context = {
        'members':members
    }
    return render(request,'core/teams.html',context)


# def clientaccountsignup_view(request):
#     return render(request,'core/signup.html')
#
#
#
# def clientaccountsignin_view(request):
#     return render(request,'core/signin.html')
#
#
# def myaccount_view(request):
#     return render(request,'core/myaccount.html')
