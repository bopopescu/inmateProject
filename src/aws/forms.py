from django import forms
from models import AWSModel
import boto


class AWSForm(forms.ModelForm):
    class Meta:
        model = AWSModel
        fields = ['aws_access_key', 'aws_secret_key']

        def clean_aws_key(self):
            aws_key = self.cleaned_data.get("aws_access_key")
            if aws_key == " " or aws_key is None:
                raise forms.ValidationError("Please enter aws keys")
            return aws_key

        def clean_secret_key(self):
            secret_key = self.cleaned_data.get("aws_secret_key")
            if secret_key == " " or secret_key is None:
                raise forms.ValidationError("Please enter aws keys")
            return secret_key


class AWSHomeForm(forms.Form):
    def __init__(self,*args, **kwargs):
        choices = kwargs.pop('my_choices')
        super(AWSHomeForm, self).__init__(*args, **kwargs)
        self.fields["aws_zone"] =choices
