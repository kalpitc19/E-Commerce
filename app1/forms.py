from django import forms
from .models import User_details


class MyForm(forms.ModelForm):
    class Meta:
        model = User_details
        fields = ["fullname", "email", "phone", "address"]
        labels = {'fullname': "Name", 'email': "Email",
                  "phone": "Mobile Number", 'address': "Local address"}
