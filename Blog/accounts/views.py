#from Blog import accounts
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':   # form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # directly creates a new user and saves in database and also return thr user
            #login user
            login(request, user)
            return redirect('articles:list')  # redirects to articles page
    elif request.method == 'GET':
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # here data is used bcz request.POST is not the first expected parameter of this function
        if form.is_valid():
            # user login
            user = form.get_user()        # gets user
            login(request, user)           # auto log in
            if 'next' in request.POST:     #redirects in this case to create page whuch requires login
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('articles:list')