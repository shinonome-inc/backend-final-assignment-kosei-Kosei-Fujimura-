from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        print(form.cleaned_data)
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)  # スペルミスに注意
        login(self.request, user)
        return response
