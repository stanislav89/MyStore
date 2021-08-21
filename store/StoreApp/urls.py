from django.contrib import admin
from django.urls import path
from .views import HomePageListView, ProductCreateView, AddProductView, ProductDetailView, \
    ProductUpdateView, ProductDeleteView, StoreLoginView, RegisterUserView, UserLogoutView, PurchaseView, \
    UserAccountView, SmartphonesListView, LaptopsListView, GadgetsListView, AudioListView, PhotoVideoListView

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('smartphones/', SmartphonesListView.as_view(), name='smartphones'),
    path('laptops/', LaptopsListView.as_view(), name='laptops'),
    path('gadgets/', GadgetsListView.as_view(), name='gadgets'),
    path('audio/', AudioListView.as_view(), name='audio'),
    path('photo-video/', PhotoVideoListView.as_view(), name='photo_video'),
    path('edit-page', ProductCreateView.as_view(), name='edit_page'),
    path('create', AddProductView.as_view(), name='create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='description'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='delete'),
    path('login', StoreLoginView.as_view(), name='login_page'),
    path('register', RegisterUserView.as_view(), name='register_page'),
    path('logout', UserLogoutView.as_view(), name='logout_page'),
    path('purchase', PurchaseView.as_view(), name='purchase_page'),
    path('account/', UserAccountView.as_view(), name='account'),
]
