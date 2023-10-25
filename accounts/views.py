from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # Use the custom form instead of the default UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
  