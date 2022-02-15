from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from second_app.forms import OrderForm
from .models import *
from second_app import models

from dashboard_app.forms import *

from django.contrib import messages


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        users = Order.objects.filter(user=request.user,ordered=True)
        total=0
        for i in users:
            s=Package.objects.get(id=i.order_package.id)
            total=total+s.price
        all_order=Order.objects.filter(ordered=True)
        admin_total=0
        for i in all_order:
            s=Package.objects.get(id=i.order_package.id)
            admin_total=admin_total+s.price
        context = {
            'service': users,
            'total':total,
            'admin_order':all_order,
            'admin_income':admin_total,
            'admin_total_user':User.objects.all(),
            'admin_pending_payment':Order.objects.filter(ordered=False)
        }
        return render(request, 'dashboard_app/index.html', context)
    else:
        return redirect('login')


def Feedbackview(request):
    try:
        prof = Profile.objects.get(user=request.user)
        if request.method == "POST":
            form = FeedbackForm(request.POST or None)
            print("form e dukse")
            if form.is_valid():
                form_user = form.save(commit=False)
                form_user.name = request.user
                form_user.photo = prof.img
                form_user.save()
                messages.success(request, "Feedback saved successfully,Wait for admin Approval", extra_tags="feedback")
                return redirect('feedback')
        else:
            form = FeedbackForm()
        return render(request, 'dashboard_app/feedback.html', {'form': form})
    except:
        return redirect('feedback')


def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    form = ProfileUpdate(instance=user_profile)
    if request.method == "POST":
        form = ProfileUpdate(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully!')
            return redirect('profile')
    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile, })


def manage_user(request):
    if request.user.is_superuser:

        users = User.objects.all()
        context = {
            'user': users,
        }
        return render(request, 'dashboard_app/manage_user.html', context)
    else:
        return redirect('dashboard')


def add_user(request):
    form = AddUser()
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'User Added Succefully!')
            return redirect('add_user')
    return render(request, 'dashboard_app/add_user.html', {'form': form, })


def verified_user(request):
    v_user = User.objects.all()

    print("-----------", v_user)
    return render(request, 'dashboard_app/verified_user.html', {'v_user': v_user})


def user_details(request, pk):
    user = User.objects.get(id=pk)
    form = UpdateUserForm(instance=user)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'User profile updated successfully!')

            return redirect('manage_user')

    return render(request, 'dashboard_app/user_details.html', {'form': form})


def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect(reverse('manage_user'))


def add_slider(request):
    slider = HomePageTopSlider.objects.all()
    if request.method == "POST":
        form = AddSlider(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slider added successfully!')
    else:
        form = AddSlider()
    return render(request, 'dashboard_app/add_homepage_slider.html', {'form': form, 'slider': slider, })


def delete_img(request, pk):
    slider_img = HomePageTopSlider.objects.get(id=pk)
    slider_img.delete()
    messages.info(request, 'Delete home page slider')
    return redirect('add_slider')


def add_homepage_complete(request):
    homepagecomplete = HomePageWeComplete.objects.all()
    if request.method == "POST":
        form = AddHOmePageComplete(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slider added successfully!')
    else:
        form = AddHOmePageComplete()
    return render(request, 'dashboard_app/add_homepage_complete.html',
                  {'form': form, 'homepagecomplete': homepagecomplete})


def delete_homepage_complete(request, pk):
    homepage_complete = HomePageWeComplete.objects.get(id=pk)
    homepage_complete.delete()
    messages.info(request, "Succefully deleted!")
    return redirect('home_page_complete')


def add_youcan_get(request):
    can_get = HomePageYouGet.objects.all()
    if request.method == "POST":
        form = AddYouCanGet(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Added successfully!')
    else:
        form = AddYouCanGet()
    return render(request, 'dashboard_app/add_you_can_get.html', {"form": form, 'can_get': can_get, })


def delete_youcan_get(request, pk):
    delete_can_get = HomePageYouGet.objects.get(id=pk)
    delete_can_get.delete()
    messages.info(request, "Succefully deleted!")
    return redirect('youcan_get')


def add_achivement(request):
    achivement = Achievement.objects.all()
    form = AddAchivement()
    if request.method == "POST":
        form = AddAchivement(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "added successfully")
            return redirect('add_achivement')

    return render(request, 'dashboard_app/add_achivement.html', {'form': form, 'achivement': achivement})


def delete_achivement(request, pk):
    del_achiv = Achievement.objects.get(id=pk)
    print("-=================", del_achiv)
    del_achiv.delete()
    messages.info(request, 'Deleted successfully')
    return redirect('add_achivement')


def add_client_review(request):
    return render(request, 'dashboard_app/add_client_review.html')


def add_footer_seciton(request):
    footer_obj = Footer.objects.all()
    form = AddFooter()
    if request.method == "POST":
        form = AddFooter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Succefully Added')
    return render(request, 'dashboard_app/add_footer_section.html', {'form': form, 'footer_obj': footer_obj})


def edit_footer_section(request, pk):
    footer = Footer.objects.get(id=pk)
    print("===============", footer)

    if request.method == "POST":
        form = AddFooter(request.POST, request.FILES, instance=footer)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your informaiton updated successfully!')
            return redirect('add_footer_section')
        else:
            messages.warning(request, 'Your form is valid !')
            return redirect('add_footer_section')
    else:
        form = AddFooter(instance=footer)

    return render(request, 'dashboard_app/edit_footer_section.html', {'form': form})


def manage_product(request):
    product = Product.objects.all()
    basic_p = BasicProduct.objects.all()
    standered_p = StanderdProduct.objects.all()
    pro_p = ProProduct.objects.all()

    context = {
        'product': product,
        'basic_p': basic_p,
        'standered_p': standered_p,
        'pro_p': pro_p,
    }
    return render(request, 'dashboard_app/manage_product.html', context)


def delete_product(request, pk):
    p = Product.objects.get(id=pk).delete()
    messages.info(request, 'Your product deleted successfully')
    return redirect('manage_product')


def edit_basic_product_info(request, pk):
    b_p = BasicProduct.objects.get(id=pk)
    form = ProductBasicForm(instance=b_p)
    if request.method == "POST":
        form = ProductBasicForm(request.POST, instance=b_p)
        form.save()
        messages.info(request, 'Successfully changed!')
        url = f"/dashboard/edit-basic-product-info/{pk}/"
        return redirect('manage_product')
    return render(request, 'dashboard_app/edit_product_info.html', {"form": form})


def edit_standered_product_info(request, pk):
    s_p = StanderdProduct.objects.get(id=pk)
    form = ProductStanderdForm(instance=s_p)
    if request.method == "POST":
        form = ProductBasicForm(request.POST, instance=s_p)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully changed!')
            url = f"/dashboard/edit-basic-product-info/{pk}/"
            return redirect('manage_product')
    return render(request, 'dashboard_app/edit_product_info.html', {"form": form})


def edit_pro_product_info(request, pk):
    p_p = ProProduct.objects.get(id=pk)
    form = ProductProForm(instance=p_p)
    if request.method == "POST":
        form = ProductBasicForm(request.POST, instance=p_p)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully changed!')
            url = f"/dashboard/edit-basic-product-info/{pk}/"
            return redirect('manage_product')
    return render(request, 'dashboard_app/edit_product_info.html', {"form": form})


def add_product(request):
    form = AddProductForm()
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Product added successfully!')
            return redirect('add_product')

    return render(request, 'dashboard_app/add_product.html', {'form': form})


def add_product_info(request):
    form_a = ProductBasicForm()
    form_b = ProductStanderdForm()
    form_c = ProductProForm()
    if request.method == "POST":
        form_a = ProductBasicForm(request.POST)
        form_b = ProductStanderdForm(request.POST)
        form_c = ProductProForm(request.POST)
        if form_a.is_valid() and form_b.is_valid() and form_c.is_valid():
            form_a.save()
            form_b.save()
            form_c.save()
            messages.info(request, 'Updated product informaiton!')
            return redirect('add_product_info')
    context = {
        'form_a': form_a,
        'form_b': form_b,
        'form_c': form_c,
    }
    return render(request, 'dashboard_app/add_product_info.html', context)


def Myorderview(request):
    my_orders=Order.objects.filter(user=request.user,ordered=True)
    context={
        'orders':my_orders,
    }
    return render(request, 'dashboard_app/myorder.html',context)


def Manageorder(request):
    if request.user.is_superuser:
        all_orders=Order.objects.all()
        context={
            'all_orders':all_orders,
        }
        return render(request,'dashboard_app/manageorder.html',context)
    else:
        return redirect('index')
def UpdateOrder(request,id):
    if request.user.is_superuser:
        orders=Order.objects.get(id=id)
        if request.method=="POST":
            form=OrderForm(request.POST or None,instance=orders)
            if form.is_valid:
                form.save()
                messages.success(request,"Order Update successfully",extra_tags="order")
                return redirect('manage-order')
        else:
            form=OrderForm(instance=orders)
        context={
            'form':form,
        }
        return render(request,'dashboard_app/updateorder.html',context)
    else:
        return redirect('index')