from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost


def registration_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
            print("form wasn't valid")
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        print('form loaded')
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def update_account_view(request):

    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.initial = {
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'username': request.POST['username'],
                'email': request.POST['email'],
            }
            form.save()
            context['success_message'] = 'Successfully updated'

    else:
        form = AccountUpdateForm(
            initial={
                'email': user.email,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        )
    context['account_form'] = form
    # blog_posts = BlogPost.objects.filter(author=user)
    blog_posts = BlogPost.objects.all()
    context['blog_posts'] = blog_posts
    return render(request, 'account/account.html', context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})
