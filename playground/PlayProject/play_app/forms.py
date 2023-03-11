from django import forms
from play_app.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()