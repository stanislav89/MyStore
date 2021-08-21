from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


from StoreApp.forms import ProductForm, LoginUserForm, RegisterUserForm, PurchaseForm
from StoreApp.models import Product, User, Purchase
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class SmartphonesListView(ListView):
    model = Product
    template_name = 'smartphones.html'
    context_object_name = 'smartphones_list'


class LaptopsListView(ListView):
    model = Product
    template_name = 'laptops.html'
    context_object_name = 'laptops_list'


class GadgetsListView(ListView):
    model = Product
    template_name = 'gadgets.html'
    context_object_name = 'gadgets_list'


class AudioListView(ListView):
    model = Product
    template_name = 'audio.html'
    context_object_name = 'audio_list'


class PhotoVideoListView(ListView):
    model = Product
    template_name = 'photo_video.html'
    context_object_name = 'photo_video_list'


class HomePageListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'list_of_products'

    def get_context_data(self, **kwargs):
        kwargs['list_of_products'] = Product.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Product
    template_name = 'edit_page.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        kwargs['list_of_products'] = Product.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'description.html'
    context_object_name = 'product_description'


class AddProductView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Product
    template_name = 'create.html'
    form_class = ProductForm
    success_url = reverse_lazy('edit_page')

    def get_context_data(self, **kwargs):
        kwargs['list_of_products'] = Product.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login_page')
    model = Product
    template_name = 'create.html'
    form_class = ProductForm
    success_url = reverse_lazy('edit_page')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login_page')
    model = Product
    template_name = 'create.html'
    success_url = reverse_lazy('edit_page')


class StoreLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class PurchaseView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase.html'
    context_object_name = 'purchase'
    success_url = reverse_lazy('account')

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):
        user_input_amount = request.POST.get('input_amount')
        user_input_amount = int(user_input_amount)
        user_id = request.POST.get('buyer')
        user = User.objects.filter(id=user_id).first()
        user_money = user.money
        product_id = request.POST.get('product')
        product = Product.objects.filter(id=product_id).first()
        product_amount = product.amount
        product_price = product.price
        final_price = user_input_amount * product_price

        if product_amount >= user_input_amount:
            if user_money >= final_price:
                product.amount -= user_input_amount
                user.money -= final_price
                purchase = Purchase.objects.create(buyer=user, product=product,
                                                   input_amount=user_input_amount, final_price=final_price)
                user.save()
                product.save()
                purchase.save()
            else:
                messages.info(self.request, 'Final price is more, than your money!')
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.info(self.request, 'Amount of product is less than you need!')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


class UserAccountView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login_page')
    model = Purchase
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        orders = Purchase.objects.filter(buyer=request.user)
        return render(request, 'account.html', {
            'orders': orders.order_by('-id')
        })
