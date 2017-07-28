from django.utils import timezone


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.utils.text import slugify



class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	address = models.CharField(max_length=255, blank=False)
	city = models.CharField(max_length=100)
	postcode = models.CharField(max_length=20)
	phone = models.IntegerField(unique=True)
	region = models.CharField(max_length=255)
	country = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# manager_obj = UserProfileManager()

	def __unicode__(self):
		return self.user 

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class BusinessLoan(models.Model):
	CHOICE_RENT = (
		('rent', 'Rent'),
		('with_mortgage', 'Own with Mortgage'),
		('without_mortgage', 'Own without Mortgage'),
		('none', 'Don\'t pay rent or Mortgage')
	) 
	full_name = models.ForeignKey(UserProfile)
	address = models.CharField(max_length=255, blank=False)
	city = models.CharField(max_length=100)
	postcode = models.CharField(max_length=20)
	phone = models.IntegerField(unique=True)
	email =models.EmailField(max_length=125)
	region = models.CharField(max_length=255)
	country = models.CharField(max_length=150)
	status = models.CharField(max_length=30, choices=CHOICE_RENT, default='rent')
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.status



	# def get_absolute_url(self):
 #        return reverse("loans_app:detail", kwargs={"slug": self.slug})
