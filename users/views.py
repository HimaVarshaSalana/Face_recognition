from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from .forms import CardDetailsForm

def register(request):
    if request.method == 'POST':
        r_form = UserRegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            username = r_form.cleaned_data.get('username')
            return redirect('carddetails')
    else:
        r_form = UserRegisterForm()     
    
    context = {
        'r_form': r_form
    }
    return render(request, 'users/register.html', context)

@login_required

def carddetails(request):
    if request.method == 'POST':
        form = CardDetailsForm(request.POST ,request.FILES, instance=request.user.carddetails)
        if form.is_valid():
            form.save()
            return redirect('app-home')
    else:
        form = CardDetailsForm()
    return render(request, 'users/carddetails.html', {'form': form})


@login_required

def profile(request):
    return render(request, 'users/profile.html')

@login_required

def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/update.html', context)
