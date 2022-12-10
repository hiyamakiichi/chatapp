from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


from .models import User
from .models import Talk, User  # Talk を追加

# ...

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)


class LoginForm(AuthenticationForm):
    pass