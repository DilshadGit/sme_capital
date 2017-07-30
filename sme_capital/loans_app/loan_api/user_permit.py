from rest_framework.permissions import ( 
	BasePermission,
	SAFE_METHODS,
)

'''
This part has nothing to do with user authenticated and is_staff or is_superuser
Here we will give each user has loggedin to update delete view own api when is created.
'''
class IsOwnerOrReadOnly(BasePermission):
	message = 'You have only permissions for your own objects!'

	user_safe_edit = ['PUT']
	def has_permission(self, request, view):
		if request.method in self.user_safe_edit:
			return True
		return False


	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.user == request.user
