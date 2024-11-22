from django.shortcuts import render, redirect

# Create your views here.
from . forms import UserInfoForm

def user_form(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sucess")
        else:
            form = UserInfoForm()
            return render(request, "user_form.html", {'form': form})
    else:
       return render(request , "user_form.html")
    
def sucess(request):
    return render(request , "sucess.html")
