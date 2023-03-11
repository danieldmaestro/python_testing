from django.shortcuts import render
from django.http import HttpResponse
from play_app.models import User
from play_app import forms

# Create your views here.
def index(request):
    form = forms.UserForm()

    if request.method == "POST":
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'play_app/index.html', {'form': form})
    

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_info': user_list}
    return render(request, 'play_app/user.html', context=user_dict)
