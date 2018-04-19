from rest_framework import generics
from usermodels.models import CustomUser
from .serializers import CustomUserSerializer
class RudCustomUserApiView(generics.RetrieveUpdateAPIView):
	lookup_field='pk'
	serializer_class=CustomUserSerializer
	# queryset= CustomUser.objects.all()
	def get_queryset(self):

		return CustomUser.objects.all()

	# def get_object(self):
	# 	pk=self.kwargs.get('pk')
	# 	return CustomUser.objects.get(pk=pk)

class CreateCustomUserApiView(generics.CreateAPIView):
	lookup_field='pk'
	serializer_class=CustomUserSerializer
	def get_queryset(self):

		return CustomUser.objects.all()


