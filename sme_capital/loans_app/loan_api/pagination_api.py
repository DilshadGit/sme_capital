from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
)

class BusniessLoanOffsetPagination(LimitOffsetPagination):
	default_limit = 3
	max_limit = 10


class BusinessLoanPageNumberPagination(PageNumberPagination):
	page_size = 3
