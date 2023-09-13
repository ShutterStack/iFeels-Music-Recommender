from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def execute_python_file(request):
    if request.method == 'POST':
        # Execute the Python file using subprocess
        result = subprocess.run(['python', 'inference.py'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        return HttpResponse(output)

    return render(request, 'dashboard.html', execute_python_file)

# Create your views here.
def camera(request):
    return render(request, 'camera.html')
    # return HttpResponse("This is Sign_in Page.")


def forgot(request):
    return render(request, 'forgot.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def inference(request):
    return render(request, 'inference.py')





