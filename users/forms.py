from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import pytz

# TIMEZONE_CHOICES = [(x, x) for x in pytz.common_timezones]

# class UserCreationForm(UserCreationForm):
#     timezone = forms.ChoiceField(choices=TIMEZONE_CHOICES, label="Timezone", required=True)
#     # timezone = forms.ChoiceField(choices=[(x, x) for x in pytz.common_timezones], required=True)

#     class Meta:
#         model = User
#         fields = ("username", "timezone", "password1", "password2")

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.timezone = timezone
#         if commit:
#             user.save()
#         return user