from rest_framework.serializers import ModelSerializer

from loans_app.models import BusinessLoan


class BusinessLoanCreateSerializer(ModelSerializer):
	
	class Meta:
		model = BusinessLoan 
		fields = [
			'user',
			'title',
			'amount',
			'start_date',
			'end_date',
			'repayment',
			'status',
			'reference',
			'phone',
			'created_date',
		]


class BusinessLoanListSerializer(ModelSerializer):
	
	class Meta:
		model = BusinessLoan 
		fields = [
			'user',
			'title',
			'slug',
			'amount',
			'start_date',
			'end_date',
			'repayment',
			'status',
			'reference',
			'phone',
			'created_date',
		]

class BusinessLoanDetailSerializer(ModelSerializer):
	
	class Meta:
		model = BusinessLoan 
		fields = [
			'user',
			'title',
			'amount',
			'start_date',
			'end_date',
			'repayment',
			'status',
			'reference',
			'phone',
			'created_date',
		]


