from rest_framework.views import APIView
from.models import Package,Subscription
from .serializers import PackageSerializer,SubscriptionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone



class PackageView(APIView):
    def get(self,request):
        packages=Package.objects.filter(is_enable=True)
        serializer=PackageSerializer(packages,many=True)
        return Response(serializer.data)


class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        subscriptions=Subscription.objects.filter(
            user=request.user,
            expire_time=timezone.now()
            #for showing active subscription
        )
        serializer=SubscriptionSerializer(subscriptions,many=True)
        return Response(serializer.data)



