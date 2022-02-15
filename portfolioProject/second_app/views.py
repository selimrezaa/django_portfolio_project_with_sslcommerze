# login functionnality
from decimal import Decimal

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_python.payment import SSLCSession
from second_app.forms import *
from django.contrib import messages
# email
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# user model
UserModel = get_user_model()
from dashboard_app.models import Feedback
# password reset
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView


# Create your views here.


def index(request):
    slider = HomePageTopSlider.objects.all()
    home_page_get = HomePageYouGet.objects.all()
    we_complete = HomePageWeComplete.objects.all()
    achivement = Achievement.objects.all()
    feedback = Feedback.objects.filter(status=True)
    context = {
        'slider': slider,
        'home_page_get': home_page_get,
        'we_complete': we_complete,
        'achivement': achivement,
        'feedback': feedback,

    }
    return render(request, 'second_app/index.html', context)


def sign_up(request):
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user_profile = Profile(user=user).save()
            current_site = get_current_site(request)
            email_sub = 'Account Created Successfully!'
            message = render_to_string('first_app/email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(email_sub, message, to=[send_mail])
            email.send()
            return render(request, 'first_app/after_signup_activeyouraccount.html')

    else:
        form = SignUpForm()
    dict = {'form': form, 'registered': registered}
    return render(request, 'first_app/signup.html', context=dict)


def test2(request):
    return render(request, 'first_app/password_reset.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)


    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.info(request, 'Your account hass been activate now!')

        return redirect('login')
    else:
        messages.warning(request, '')

        return HttpResponse('activation code is incorrect!')


# def resetcomplete(request):
#     messages.info(success, 'Weldone! You are successfully changed your password!')
#     return redirect('login')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                next = request.GET.get("next", '')
                print(next)
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)

                    if next != "":
                        return redirect(next)
                    return redirect('dashboard')
        else:
            form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'first_app/login.html', context)


from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# Client side functionality

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *


def service(request):
    product = Services.objects.all().order_by("-id")
    context = {
        'services': product,
    }
    return render(request, 'second_app/service.html', context)


def our_work(request):
    work = OurWork.objects.all()
    work_list = WorkList.objects.all()

    return render(request, 'second_app/work.html', {'work_list': work_list, 'work': work, })


def team_member(request):
    members = TeamMember.objects.all()
    context = {
        'members': members
    }
    return render(request, 'second_app/team_member.html', context)


def about_us(request):
    obj = AboutUs.objects.last()
    return render(request, 'second_app/about_us.html', {'obj': obj})


@login_required(login_url='login')
def checkout(request, service_id, package_id):
    try:
        pro=Profile.objects.get(user=request.user)
        if pro.is_fully_filled()==True:
            service = Services.objects.get(id=service_id)
            package = Package.objects.get(id=package_id)
            ord = Order()
            ord.order_service = service
            ord.order_package = package
            ord.user = request.user
            ord.save()
            return redirect(ord.get_payment_url())
        else:
            messages.warning(request,"First complete your profile to Buy",extra_tags="profile-complete")
            return redirect('profile')
    except:
        return redirect('service')


@login_required()
def payment(request, id):
    my_order = Order.objects.get(id=id)
    store_id = 'js61323dab467ae'
    API_key = 'js61323dab467ae@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)
    status_url = request.build_absolute_uri(reverse('complete'))
    # print(status_url)
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

    mypayment.set_product_integration(total_amount=Decimal(my_order.order_package.price), currency='BDT',
                                      product_category='Mixed',
                                      product_name=my_order.order_service, num_of_item=1,
                                      shipping_method='Courier', product_profile='None')

    current_user = request.user
    print()

    mypayment.set_customer_info(name=current_user.user_profile.first_name, email=current_user.email,
                                address1="None", address2="None",
                                city=current_user.user_profile.city, postcode=current_user.user_profile.zip_code,
                                country=current_user.user_profile.country, phone=current_user.user_profile.phone)

    mypayment.set_shipping_info(shipping_to=current_user.user_profile.first_name, address="None",
                                city=current_user.user_profile.city, postcode=current_user.user_profile.zip_code, country=current_user.user_profile.country)

    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request, f"Your Payment Completed Successfully! Page will be redirected!")
            return HttpResponseRedirect(
                reverse("purchase", kwargs={'val_id': val_id, 'tran_id': tran_id}, ))
        elif status == 'FAILED':
            messages.warning(request, f"Your Payment Failed! Please Try Again! Page will be redirected!",extra_tags="status")

    return render(request, "complete.html", context={})


@login_required
def purchase(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False).order_by("-id")
    order = order_qs[0]
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.save()
    # messages.success(request, f"Your Payment succeed! Please Check your Dashboard! Page will be redirected!", extra_tags="success")
    return render(request, "complete.html", context={})
