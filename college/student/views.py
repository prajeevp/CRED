from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Details
def homePage(request):
    template_name = 'homePage.html'
    return render(request, template_name)

def signupPage(request):
    # template_name = 'signupPage.html'
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        my_user = User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('loginPage')

    return render(request, 'signupPage.html')


def loginPage(request):
    if request.method == 'POST':    
        username = request.POST.get('username')
        passwordFinal = request.POST.get('password')
        user = authenticate(request, username=username, password=passwordFinal)
        try:
            if user is not None:
                login(request, user)
                return redirect('homePage')
            else:
                return HttpResponse("Username or password is incorrect")
        except Exception as es:
            print("::::::::::::",es)
            
    return render(request, 'login.html', {'csrf_token': request.COOKIES['csrftoken']})

def logoutPage(request):
    logout(request)
    return redirect('loginPage')  

def details_view(request):
    all_details = Details.objects.all()

    return render(request, 'all_details.html', {'all_details': all_details}) 
