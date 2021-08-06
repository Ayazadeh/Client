from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from django.views import View
from customer.permissions import *
from customer.serializers import *


# class LoginView(View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'form.html')
#
#     def post(self, request, *args, **kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username)
#         print(password)
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user:
#             login(request, user)
#             return redirect('profile')
#         return render(request, 'form.html', {'error': 'invalid login!!!'})
#
#


class ProfileView(PermissionRequiredMixin, View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, 'profile.html')


class Login(LoginView):
    template_name = 'registration/form.html'
    success_url = 'accounts/profile'


class Logout(LogoutView):
    next_page = 'my_login'


class UserListApi(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsSuperUser
    ]
    queryset = Customer.objects.all()


class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = Customer.objects.all()
    permission_classes = [
        UserDetailOwner
    ]


class AddressListApi(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def get_queryset(self):
        return Address.objects.filter(owner__user_id=self.request.user.id)


class AddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [
        AddressDetailOwner
    ]

