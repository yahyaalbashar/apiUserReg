from rest_framework import serializers
from usermodels.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

	class Meta:
		model=CustomUser

		fields=['username',
				'password',
				'email',
				'age',
				'pk'
		]

		read_only_fields=['pk','password']
	def validate_username(self,value):
	 	qs=CustomUser.objects.filter(username__iexact=value)
	 	if self.instance:
	 		qs=qs.exclude(pk=self.instance.pk)
	 	if qs.exists():
	 		raise serializers.Validation_error('username must be unique')
	 	return value