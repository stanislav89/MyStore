from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from StoreApp.forms import ArticleForm, LoginUserForm, RegisterUserForm, ProfileForm, PurchaseForm
from StoreApp.models import Articles, User, Purchase
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class HomePageListView(ListView):
    model = Articles
    template_name = 'index.html'
    context_object_name = 'list_articles'


class ProductDetailView(DetailView):
    model = Articles
    template_name = 'description.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Articles
    template_name = 'edit_page.html'
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class AddProductView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Articles
    template_name = 'create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login_page')
    model = Articles
    template_name = 'create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('edit_page')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login_page')
    model = Articles
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
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):
        user_input_amount = request.POST.get('input_amount')
        user_input_amount = int(user_input_amount)
        user_id = request.POST.get('buyer')
        user = User.objects.filter(id=user_id).first()
        user_money = user.money
        product_id = request.POST.get('product')
        product = Articles.objects.filter(id=product_id).first()
        product_amount = product.amount
        product_price = product.price
        final_price = user_input_amount * product_price
        my_error = True

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
                return 'my_error'
        else:
            return 'my_error'
        return HttpResponseRedirect(self.get_success_url())


class UserAccountView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login_page')
    model = Purchase
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        orders = Purchase.objects.filter(buyer=request.user)
        return render(request, 'account.html', {
            'orders': orders
        })

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     return context

# def edit_page(request):
#     return render(request, 'edit_page.html', {
#         'list_articles': Articles.objects.all().order_by('-id')
#     })


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_page')
#         else:
#             error = 'Form filling error!'
#
#     return render(request, 'create.html', {
#         'list_articles': Articles.objects.all().order_by('-id'),
#         'form': ArticleForm,
#         'error': error,
#     })


# def update_product(request, pk):
#     get_article = Articles.objects.get(pk=pk)
#     error = ''
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, instance=get_article)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_page')
#         else:
#             error = 'Form filling error!'
#     return render(request, 'edit_page.html', {
#         'get_article': get_article,
#         'update': True,
#         'form': ArticleForm(instance=get_article),
#         'error': error,
#     })


# def delete_product(request, pk):
#     get_article = Articles.objects.get(pk=pk)
#     get_article.delete()
#     return redirect('edit_page')
