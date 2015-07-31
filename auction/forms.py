from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), 
		label="Username", error_messages={ 'invalid': ("This value must contain only letters, \
			numbers and underscores.") })
	firstname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), 
		label="First Name")
	lastname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), 
		label="Last Name")
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), 
		label="Email Address")
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,
		render_value=False)), label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, 
		render_value=False)), label="Re-enter Password")

	def clean_username(self):
		err_msg = "The username already exists. Please try something else"
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(err_msg)

	def clean(self):
		err_msg = "The two passwords do not match. Please re-enter"
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(err_msg)
		return self.cleaned_data