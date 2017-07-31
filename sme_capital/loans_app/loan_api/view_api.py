from django.db.models import Q

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
)
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
from .pagination_api import ( 
	BusniessLoanOffsetPagination,
	BusinessLoanPageNumberPagination,
)
from .user_permit import IsOwnerOrReadOnly
from .serializers import ( 
	BusinessLoanCreateSerializer,
	BusinessLoanDetailSerializer,
	BusinessLoanListSerializer,
)


class BusinessLoanCreateAPIView(CreateAPIView):
	queryset = BusinessLoan.objects.all()
	serializer_class = BusinessLoanCreateSerializer
	permission_classes = [IsAuthenticated]

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
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class BusinessLoanListAPIView(ListAPIView):
	
	serializer_class = BusinessLoanListSerializer
	filter_backebds = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'reference', 'start_date', 'end_date']
	# pagination_class = BusniessLoanOffsetPagination # PageNumberPagination
	pagination_class = BusinessLoanPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		querysets = BusinessLoan.objects.all()
		query = self.request.GET.get('q')
		if query:
			querysets = querysets.filter(
				Q(title__icontains=query)|
				Q(reference__icontains=query)|
				Q(start_date__icontains=query)|
				Q(end_date__icontains=query)
			).distinct()
		return querysets





