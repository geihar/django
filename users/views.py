from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegForm, UserUpdate, ProfileImg
from main_page.models import AsideNews


def registration(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('log')
    else:
        form = UserRegForm()
        data = {'form': form, 'title': 'Регистрация пользователя', 'aside': AsideNews.objects.order_by("text")[:2]}
    return render(request, 'users/registration.html', data)


@login_required
def profile(request):
    if request.method == "POST":
        img_prolile = ProfileImg(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdate(request.POST, instance=request.user)
        if update_user.is_valid() and img_prolile.is_valid():
            update_user.save()
            img_prolile.save()
            messages.success(request, f'Ваш аккаунт был обновлен')
            return redirect(profile)
    else:
        img_prolile = ProfileImg(instance=request.user.profile)
        update_user = UserUpdate(instance=request.user)
        data = {'img_prolile': img_prolile, 'update_user': update_user, 'aside': AsideNews.objects.order_by("title")[:4]}

        return render(request, 'users/profile.html', data)
