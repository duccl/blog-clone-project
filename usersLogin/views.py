from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect

class LoginView(FormView):
    success_url = "posters/"
    form_class = AuthenticationForm

    template_name = "usersLogin/login.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse("posters:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("posters:home"))
