from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
	"""退出登录"""
	logout(request)
	return HttpResponseRedirect(reverse("index"))


def register(request):
	if request.method != "POST":
		form = UserCreationForm()
	else:
		form = UserCreationForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			authenticate_user = authenticate(username=new_user.username, password=request.POST["password1"])
			login(request, authenticate_user)
			return HttpResponseRedirect(reverse("index"))

	context = {"form":form}
	return render(request, "users/register.html", context)