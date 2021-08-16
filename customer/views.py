from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import generics
from django.views import View
from django.views.generic import CreateView, UpdateView
from customer.permissions import *
from customer.serializers import *
from customer.forms import *


class UserChange(LoginRequiredMixin, UpdateView):
    template_name = 'customer/user_edit.html'
    success_url = reverse_lazy('customer:profile')
    form_class = NewUserChangeForm
    model = Customer


class ProfileView(LoginRequiredMixin, View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        address = Customer.objects.get(user_ptr_id=self.request.user.id)
        return render(request, 'customer/profile.html', {'address': address})


class Login(LoginView):
    """
    template name default is registration/login.html
    """
    pass


class Logout(LogoutView):
    next_page = reverse_lazy('customer:my_login')


class RegisterView(CreateView):
    template_name = 'customer/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('customer:my_login')


class AddressView(CreateView):
    template_name = 'customer/address.html'
    form_class = AddressForm
    success_url = reverse_lazy('customer:profile')

    def form_valid(self, form):
        address = form.save(commit=False)
        address.owner = Customer.objects.get(user_ptr_id=self.request.user.id)
        return super().form_valid(form)


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

# class NewLoginView(View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'registration/login.html')
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
#             return redirect('customer:profile')
#         return render(request, 'registration/login.html', {'error': 'invalid login!!!'})


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = RegisterForm()
#     return render(request, 'customer/register.html', {'form': form})
