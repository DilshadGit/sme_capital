from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User 
from .models import UserProfile
from .forms import EditProfileForm, LoanForm


def profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
		
	context = {
		'user': user,
	}
	return render(request, 'profile.html', context)


def edit_profile(request):

	if request.method == 'POST':
		edit_form = EditProfileForm(request.POST, instance=request.user)

		if edit_form.is_valid():
			edit_form.save()
			update_session_auth_hash(request, edit_form.user)
			return redirect('loans_app:profile')
	else:
		edit_form = EditProfileForm(instance=request.user)
	context  = {
		'edit_form':edit_form,
	}
	return render(request, 'edit_profile.html', context)


def create_loan(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = LoanForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}

	return render(request, 'create_loans.html', context)


