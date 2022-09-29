from django import forms


from main.models import Complain


class ComplainForm(forms.ModelForm):
    """form for submission of complain"""
    class Meta:
        model = Complain
        fields = "__all__"