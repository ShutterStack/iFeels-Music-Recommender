from django.shortcuts import render, HttpResponse


# Create your views here.
def camera(request):
    return render(request, 'camera.html')
    # return HttpResponse("This is Sign_in Page.")

def dashboard(request):
   # return render(request, 'dashboard.html')
    # if request.method == 'POST':
    #     # Execute the Python file using subprocess
    #     result = subprocess.run(['python', 'inference.py'], stdout=subprocess.PIPE)
    #     output = result.stdout.decode('utf-8')
    #     return HttpResponse(output)

    return render(request, 'dashboard.html')

def forgot(request):
    return render(request, 'forgot.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

