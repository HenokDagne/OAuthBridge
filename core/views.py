
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import ProfileSerializer
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect, render
from .models import Profile
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import requests

# Create your views here.
 
def google_logout(request):
    # Revoke the Google token (if available)
    social_account = request.user.socialaccount_set.filter(provider='google').first()
    if social_account:
        token = social_account.socialtoken_set.first()
        if token:
            revoke_url = 'https://accounts.google.com/o/oauth2/revoke'
            params = {'token': token.token}
            requests.post(revoke_url, params=params)

    # Log out the user from Django
    logout(request)
    return redirect('/')

class Home(APIView):
    def get(self, request):
        message = "Home page"
        return render(request, 'home.html', {'message': message})



class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()  # Define the queryset
    serializer_class = ProfileSerializer
    permission_class = [IsAuthenticated]

    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)
    

    def permission_denied(self, request, message=None, code=None):
        if not request.user.is_authenticated:
            raise NotAuthenticated(detail="you must be login to access this page. please login in at at /auth/jwt/create")
        super().permission_denied(request, message, code)
  

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
  

       
   

    

        


    
    