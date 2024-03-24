from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (
    CustomUser,
)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        # fields = ('username', 'email', "avatar")
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = ('username', 'email', "avatar",)
        fields = "__all__"
        # kafedra = forms.ModelMultipleChoiceField(queryset=Kafedra.objects.all(), required=False)
