from django.contrib.auth.forms import User
from django.contrib.auth.models import Group

from django.shortcuts import get_object_or_404, render, redirect
from .forms import DoctorForm, PatientForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Post
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils.text import slugify



# Create your views here.

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                  
                                   publish__year=year, 
                                   publish__month=month,
                                   publish__day=day,
    )
    context = {
        'post': post,
    }
    return render(request, 'account/post_detail.html', context)

@login_required(login_url='account:home')
def makeBlog(request):
    visitor = request.user

    namer = Doctor.objects.get(email__startswith=visitor.email)

    if request.method == "POST":
        form  = BlogForm(request.POST)
        
        if form.is_valid():
            form = BlogForm(request.POST)
            post = form.save(commit=False)
            post.author = namer
            post.slug = slugify(post.title)
            post.save()
            
            
            messages.info(request, "Created a blog successfully")
            return redirect('account:home')

    else:     
        form = BlogForm()
    context  = {
        'form': form,
    }

    return render(request, 'account/blog.html', context)




def home(request):
    visitor = request.user
    form = None
    flag = False
    
    if request.user.is_anonymous or request.user.is_staff:
        blog = None
    else:
        try:
            form = Doctor.objects.get(email__startswith=visitor.email)
            if form is not None: 
                blog = Post.objects.all().order_by('-created_on')
                flag = True
           
        except Doctor.DoesNotExist:
            form = Patient.objects.get(email__startswith=visitor.email)
            if form is not None:
                blog = Post.objects.filter(status=1).order_by('-created_on')

    
    
    context = {'blog': blog,
                'flag': flag,
                
    }
    return render(request, 'account/home.html', context)



def loginPage(request):
    

    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
 
                return redirect('account:dashboard')
            else:
                messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'account/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('account:login')

@login_required(login_url='account:home')
def dashboard(request):
    visitor = request.user
    form = None
    flag = False
    try:
        form = Doctor.objects.get(email__startswith=visitor.email)
        flag = True
    except Doctor.DoesNotExist:
        form = Patient.objects.get(email__startswith=visitor.email)

    
     
    context = {'form': form,
                'flag':flag
    }
    return render(request, 'account/dashboard.html', context)


 

def Choose(request):
    context = {}
    return render(request, 'account/select.html', context)


def registerDoctor(request):
    
    if request.method == "POST":
        form = DoctorForm(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1 == password2 and password1 != "":


            if form.is_valid():
                form.save()
            
            
            email = form.cleaned_data.get('email')

            

            user = User.objects.create_user(username=username, email=email, password = password1)                               
                                            
            user.save()

        

            messages.info(request,"An Account is Created Successfully")


            return redirect('account:dashboard')
        else:
            messages.info(request,"Password does not match, Try Again")
            return redirect('account:doctor')        
    else:
        form = DoctorForm()
    
    context = {'form':form}
    return render(request, 'account/register.html', context)


def registerPatient(request):
    
    if request.method == "POST":
        form = PatientForm(request.POST)

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2 and password1 != "":

                if form.is_valid():
                    form.save()
                
               
                email = form.cleaned_data.get('email')

                user = User.objects.create_user(username=username, email=email, password = password1)                               
                                                
                user.save()
                messages.info(request,"An Account is Created Successfully")


                return redirect('account:dashboard')
        else:
            messages.info(request,"Password does not match, Try Again")
            return redirect('account:patient')        
    else:
        form = PatientForm()
    
    context = {'form':form}
    return render(request, 'account/register.html', context)
      
        
