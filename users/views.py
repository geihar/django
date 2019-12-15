from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegForm


def registration(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('main_page')
    else:
        form = UserRegForm()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})

