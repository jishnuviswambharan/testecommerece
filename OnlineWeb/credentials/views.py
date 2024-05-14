
from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from .models import UserProfile

# Create your views here.

#login Page

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        log_user = auth.authenticate(username=username,password=password)

        if log_user is not None:
            auth.login(request,log_user)
            # messages.info(request,"Invalid User Name or Password")
            return redirect('/')
        else:
            messages.info(request,"Invalid User Name or Password")
            # return redirect('/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# Registration Page

# def register(request):
#     try:
#         if request.method == "POST":
#             first_name = request.POST['first_name']
#             username = request.POST['username']
#             email = request.POST['email']
#             password = request.POST['password']
#             confirm_password = request.POST['cpassword']

#             if password == confirm_password:
#                 if User.objects.filter(username==username).exists():
#                     messages.info(request, "User Name Already Exists")
#                 elif User.objects.filter(email==email).exists():
#                     messages.info(request,"Email Already Exists")
#                 else:
#                     newuser = User.objects.create_user(username=username, email=email,password=password, first_name=first_name)
#                     newuser.save()
#                     messages.info(request, "User Created Sucessfully")
#                     print("User Created Sucessfully")
#                     return redirect('login')
#             else:
#                 messages.error(request,"Passwords do not match")
#                 return redirect('login')
#         return render(request, "register.html")
#     except:
#         messages.info(request,"User Creation under progress, Please refresh the page")
#         return redirect(request,'register')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
                user.save()
                messages.success(request, "User created successfully")
                print("User created")
                return render(request,'login.html')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
    return render(request, "register.html")



# def register(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['cpassword']
#         image = request.FILES.get('image')  # Assuming 'image' is the name of your file input field in the form

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "Username already exists")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "Email already exists")
#                 return redirect('register')
#             else:
#                 # Create user
#                 user = User.objects.create_user(username=username, password=password, email=email)
#                 user.first_name = name
#                 user.save()

#                 # Create user profile with image
#                 UserProfile.objects.create(user=user, image=image)

#                 messages.success(request, "User created successfully")
#                 print("User created")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match")
#             return redirect('register')

#     return render(request, "register.html")

# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         # last_name = request.POST['last_name']
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:
#             if User.objects.filter(username__iexact=name).exists():
#                 messages.info(request, "Username already exists")
#                 return redirect('register')
#             elif User.objects.filter(email__iexact=email).exists():
#                 messages.info(request, "Email already exists")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=name, password=password, first_name=first_name, email=email)
#                 auth.login(request, user)  # Log in the user after registration if needed
#                 messages.success(request, "User created successfully")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match")
#             return redirect('register')

#     return render(request, "Register.html")