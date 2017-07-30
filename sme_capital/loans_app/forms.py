from django import forms
from django.contrib.auth.models import User 
from .models import UserProfile, BusinessLoan
from django.contrib.auth.forms import (
	UserCreationForm, 
	UserChangeForm,
)



class EditProfileForm(UserCreationForm):

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			# 'password',
		)
		exclude = ('password',)


class BusinessLoanForm(forms.ModelForm):

	class Meta:
		model = BusinessLoan
		fields = (
			'title',
			'amount',
			'start_date',
			'end_date',
			'repayment',
			'status',
			'reference',
			'phone',
		)