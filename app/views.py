from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import customer_register
from .models import event_team_reg
from .models import Login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')





def gallery(request):
    return render(request, 'gallery.html')


def events(request):
    return render(request, 'events.html')


def contact(request):
    return render(request, 'contact.html')


def error(request):
    return render(request, 'error.html')


def Login1(request):
    if request.method == 'POST':
        print('requestsss', request.POST)
        u = request.POST['n1']
        p = request.POST['n2']
        try:
            c = Login.objects.get(Username=u)
            if c.Password == p:
                if c.St == "0":
                    return render(request, 'admin.html')
                elif c.St == "1":
                    return render(request, 'events.html')
                elif c.St == "2":
                    return render(request, 'event_data.html')
                else:
                    return HttpResponse('404 error')

            else:
                return HttpResponse('invalid password')
        except Exception:
            return HttpResponse('invalid username')
    else:
        return render(request, 'Login.html')

def Logout(request):
    logout(request)
    return render(request,'index.html')


def C_Register(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        f = request.POST['n6']
        if e == f:
            user = customer_register.objects.create(Firstname=a, Lastname=b, Username=c, Email=d, Password=e,
                                                    Confirm_Password=f)
            user.save()
            user1 = Login.objects.create(Username=c, Password=e, St=1)
            user1.save()
            return render(request, 'Login.html')
        else:
            return HttpResponse("passwords does not match")
    else:
        return render(request, 'Register.html')


def E_Register(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        f = request.POST['n6']
        g = request.POST['n7']
        h = request.POST['n8']
        j = request.FILES['n9']
        k = request.FILES['m2']
        if c == h:
            user = event_team_reg.objects.create(Team_name=a, Username=b, Password=c, Email=d, Address=e, Contact=f,
                                                 License=g, status='pending',image=j,logo=k)
            user.save()
            user1 = Login.objects.create(Username=b, Password=c, St=2)
            user1.save()
            return render(request, 'Login.html')
        else:
            return HttpResponse("passwords does not match")
    else:
        return render(request, 'E_Register.html')


# def E_Details(request):
#     if request.method == 'POST':
#         a = request.POST['n1']
#         b = request.POST['n2']
#         c = request.POST['n3']
#         d = request.POST['n4']
#         e = request.POST['n5']
#         f = request.POST['n6']
#         g = request.POST['n7']
#         h = request.POST['n8']
#         i = request.POST['n9']
#
#         user = event_team_reg.objects.create(Team_name=a, address=b, district=c, pin=d, package=e, Email=f,
#                                                  Contact=g, image=h, logo=i)
#         user.save()
#         return HttpResponse('sent to admin for verification')
#



def ad_regevents(request):
    if request.method == 'GET':
        d = event_team_reg.objects.all()
        return render(request, 'registered_events.html', {'r': d})


def E_Verify(request):
    d = event_team_reg.objects.filter(status='pending')
    return render(request, 'admin_verify.html', {'r': d})


def ad_approve(request, y):
    event_team_reg.objects.filter(Username=y).update(status='confirm')
    return redirect(E_Verify)


def ad_reject(request, n):
    return HttpResponse('verification rejected')


def booking(request):
    d = event_team_reg.objects.filter(status='confirm')
    return render(request, 'booking.html',{'r':d})

# def profile(request):
#     if 'id' in request.session:
#         x=request.session['id']
#         return render(request,'profile.html')
#     else:
#         return redirect(log)