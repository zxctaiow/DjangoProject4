from django import forms
from welcome.models import News, Comments
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class NewsForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    news_title = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control-for-title", "placeholder": "News Title"}))
    news_text = forms.CharField(label='', widget=forms.Textarea(attrs={"rows" : 15, "class": "form-control-for-text", "placeholder":"News Text"}))
    class Meta:
        model = News
        fields = ['news_title', 'news_text']

class ComentCreateForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    topic = News
    comment_text = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "comment_form_control", "placeholder": "Comment Text Here"}))
    class Meta:
        model = Comments
        fields = ['topic', 'comment_text']


# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
    
#     username = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'account_login_username', 'placeholder': 'USERNAME', 'id': 'hello', 'autocomplete': 'off'}
#     ))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'account_login_password',
#             'placeholder': 'PASSWORD',
#             'id': 'hi',
#             'autocomplete': 'off'
#         }
#     ))