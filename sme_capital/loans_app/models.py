from django.utils import timezone
import datetime
from django.conf import settings
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
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


	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class BusinessLoan(models.Model):
	CHOICE_RENT = (
		('rent', 'Rent'),
		('with_mortgage', 'Own with Mortgage'),
		('without_mortgage', 'Own without Mortgage'),
		('none', 'Don\'t pay rent or Mortgage')
	)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=255, blank=False, null=False)
	slug = models.SlugField(unique=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	start_date = models.DateField(_("Date"), default=datetime.date.today)
	end_date = models.DateField(_("Date"), default=datetime.date.today)
	repayment = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	reference = models.CharField(max_length=12)
	phone = models.IntegerField(unique=True)
	status = models.CharField(max_length=30, choices=CHOICE_RENT, default='rent')
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.reference)



	def get_absolute_url(self):
		return reverse("loans_app:detail_loan", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = BusinessLoan.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_loan_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_loan_receiver, sender=BusinessLoan)
