from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse_lazy
# from django.urls import reverse
from django.contrib.auth import login, logout
from . import forms


# class HomePage(TemplateView):
#     template_name = 'index.html'


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
