from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_details
from .forms import MyForm

# Create your views here.
# class LoginView(DetailView):
#     template_name="app1/index.html"


# def my_form(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # will redirect to Product list page_______
#             return HttpResponseRedirect('login')
#     else:
#         form = MyForm()
#     return render(request, 'app1/cv_form.html', {'form': form})


# def index(request):
#     return render(request, 'app1/index.html')

def index(request):
    if (request.method == "POST"):
        add = User_details()
        add.fullname = request.POST.get('fullname')
        add.email = request.POST.get('email')
        add.phone = request.POST.get('phone')
        add.address = request.POST.get('address')
        add.save()
        return HttpResponseRedirect("/")
    return render(request, "app1/index.html")
