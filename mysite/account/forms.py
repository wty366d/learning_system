from django.contrib.auth.models import User
from django.forms import ModelForm
from account.models import UserProfile


class UserForm(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('todai_id', 'grade')
