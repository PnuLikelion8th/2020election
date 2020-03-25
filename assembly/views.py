from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def assembly(request):
    return render(request, 'quiz.html')