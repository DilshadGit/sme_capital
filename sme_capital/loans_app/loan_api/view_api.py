from rest_framework.generics import ( 
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,

)

from loans_app.models import BusinessLoan
from .user_permit import IsOwnerOrReadOnly
from .serializers import ( 
	BusinessLoanCreateSerializer,
	BusinessLoanDetailSerializer,
	BusinessLoanListSerializer,
)


class BusinessLoanCreateAPIView(CreateAPIView):
	queryset = BusinessLoan.objects.all()
	serializer_class = BusinessLoanCreateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	# this is display the user name when create new api
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class BusinessLoanDetailAPIView(RetrieveAPIView):
	queryset = BusinessLoan.objects.all()
	serializer_class = BusinessLoanDetailSerializer


class BusinessLoanEditAPIView(RetrieveUpdateAPIView):
	queryset = BusinessLoan.objects.all()
	serializer_class = BusinessLoanDetailSerializer
	
	lookup_field = 'slug'
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class BusinessLoanDeleteAPIView(DestroyAPIView):
	queryset = BusinessLoan.objects.all()
	serializer_class = BusinessLoanDetailSerializer
	lookup_field = 'slug'


class BusinessLoanListAPIView(ListAPIView):
	queryset = BusinessLoan.objects.all()
	serializer_class = BusinessLoanListSerializer





