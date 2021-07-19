from django.shortcuts import render, redirect
from ..forms import RegisterForm
# Create your views here.


def register(request):
    if request.method == 'GET':
        form = RegisterForm()

    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form
    })