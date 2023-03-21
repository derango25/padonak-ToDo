from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):

    return render(request, 'todo/signupuser.html', {'form':UserCreationForm()}) #не писать ссылку на шаблон, только корневая папка и название страницы!