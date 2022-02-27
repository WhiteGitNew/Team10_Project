
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .userform import UserForm
# Create your views here.




@login_required
def detail_profile(request):
    """look user profile detail"""
    if request.method == "POST":
        _form = UserForm(request.POST, instance=request.user)
        if _form.is_valid():
            _form.save()
        else: print(_form.errors)
    return render(request, "account/cuser_profile.html")

