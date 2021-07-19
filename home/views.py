# Create your views here.
from django.shortcuts import render,HttpResponse
from django.templatetags.static import static




# Create your views here.
def home(request):
    return render(request, 'index.html')    

# Create your views here.

    

