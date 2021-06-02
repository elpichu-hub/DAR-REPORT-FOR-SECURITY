from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'You have created an account for {username}')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)





    



