from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User 
from .models import UserProfile, BusinessLoan
from .forms import EditProfileForm, BusinessLoanForm
from django.contrib.auth.decorators import login_required


def profile(request, pk=None):

	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
		
	context = {
		'user': user,
	}
	return render(request, 'profile.html', context)


@login_required
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


@login_required
def create_loan(request):
	form = BusinessLoanForm(request.POST or None)
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



def loan_detail(request, slug=None):
	instance = get_object_or_404(BusinessLoan, slug=slug)
	context = {
		'instance': instance,
	}
	return render(request, 'loan_detail.html', context)


def loan_list(request):
	loans = BusinessLoan.objects.all()

	context = {
		'loans_obj': loans,
	}
	return render(request, 'loan_list.html', context)


@login_required
def loan_edit(request, slug=None):
	instance = get_object_or_404(BusinessLoan, slug=slug)
	form = BusinessLoanForm(request.POST or None, instance=instance)
	if form.is_valid():
	    instance = form.save(commit=False)
	    instance.save()
	    messages.success(request, 'The loan successfully updated!')
	    return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	    'title': instance.reference,
	    'instance': instance,
	    'form': form
	}
	return render(request, 'edit_loan.html', context)

@login_required
def loan_delete(request, slug=None):
	instance = get_object_or_404(BusinessLoan, slug=slug)
	instance.delete()
	messages.success(request, 'The loan has been deleted!')
	return redirect('loans_app:list_loan')
