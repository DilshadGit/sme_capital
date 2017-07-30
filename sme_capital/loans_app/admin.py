from django.contrib import admin

# Register your models here.
from .models import UserProfile, BusinessLoan 

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'address', 'city', 'postcode')

	def user_contact(self, obj):
		return obj.phone

	user_contact.short_description = 'phone'

	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('user')
		return queryset

	class Meta:
		module = UserProfile
		fields = [
			'user',
			'address',
			'city',
			'postcode',
			'phone'
		]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BusinessLoan)